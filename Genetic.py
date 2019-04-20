# This is Code Trying to Find Minima and Maxima Of a Function in A Certain Range Using Genetic Algorithm
# Our Function is:
# X^3 * cos(x) + X^2 * cos(x) - X*sin(x)
# The Code Works For Both Minima And Maxima;
# If you Want to Find Maxima Your Fitness Function Must Return The Value Of Function
# Otherwise Your Fitness Function Must Return The -Value Of Function

import math
import random
import struct
import matplotlib.pyplot as plt


def show_plot(population_list):
    x = list()
    y = list()
    for i in range(0, len(population_list)):
        x.append(float(bin_to_float(population_list[i])))
    for i in range(0, len(population_list)):
        y.append(fitness(population_list[i]))
    plt.scatter(x, y)
    plt.show()


def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')


def bin_to_float(binary):
    return struct.unpack('!f', struct.pack('!I', int(binary, 2)))[0]


def get_equation_ans(x):
    y = float(bin_to_float(x))
    return y ** 3 * math.cos(y) + y ** 2 * math.cos(y) - y * math.sin(y)


def mutation(population_list):
    for i in range(0, len(population_list)):
        probability = random.randint(0, 100000)
        if probability < 10:
            print("Mutation Executed")
            genome = population_list[i]
            index = random.randint(0, 31)
            genome = genome[0:index] + str(random.randint(0, 1)) + genome[index + 1:len(genome)]
            while not (-2 <= float(bin_to_float(genome)) <= 1):
                genome = population_list[i]
                index = random.randint(0, 32)
                genome = genome[0:index] + str(random.randint(0, 1)) + genome[index + 1:len(genome)]
            population_list[i] = genome


def crossover(population_list):
    children = list()
    for i in range(0, len(population_list) - 1, 2):
        index1 = -1
        index2 = -1
        probability = random.randint(1, 10)
        if probability <= 3:
            index1 = random.randint(0, int(len(population_list) / 2))
        else:
            index1 = random.randint(int(len(population_list) / 2), len(population_list) - 1)
        probability = random.randint(1, 10)
        if probability <= 3:
            index2 = random.randint(0, int(len(population_list) / 2))
        else:
            index2 = random.randint(int(len(population_list) / 2), len(population_list) - 1)
        genome1 = population_list[index1]
        genome2 = population_list[index2]
        index = random.randint(0, 31)
        child1 = genome1[0:index] + genome2[index:len(genome1)]
        child2 = genome2[0:index] + genome1[index:len(genome1)]
        while (not (-2 <= float(bin_to_float(child1)) <= 1)) or (not (-2 <= float(bin_to_float(child1)) <= 1)):
            index = random.randint(0, 31)
            child1 = genome1[0:index] + genome2[index:len(genome1)]
            child2 = genome2[0:index] + genome1[index:len(genome1)]
        children.append(child1)
        children.append(child2)
    for i in range(0, len(children)):
        population_list.append(children[i])


def selection(population_list):
    population_list.sort(key=fitness)
    size = int(len(population_list) / 2)
    for i in range(0, size):
        population_list.remove(population_list[0])


def fitness(genome):
    return -get_equation_ans(genome)


def generate_population(population_list, number_of_genome, range_min, range_max):
    for i in range(0, number_of_genome):
        population_list.append(float_to_bin(random.random() * (range_max - range_min) + range_min))


generation_number = int(input("Please Enter Number Of Generations:"))
genome_number = int(input("Please Enter Number Of Genomes:"))
population = list()
generate_population(population, genome_number, -2, 1)

for i in range(0, generation_number):
    show_plot(population)
    selection(population)
    crossover(population)
    mutation(population)

population.sort(key=fitness, reverse=True)
print(bin_to_float(population[0]))
