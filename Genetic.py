# This is Code Trying to Find Minima and Maxima Of a Function in A Certain Range Using Genetic Algorithm
# The Code Works For Both Minima And Maxima;
# If you Want to Find Maxima Your Fitness Function Must Return The Value Of Function
# Otherwise Your Fitness Function Must Return The -Value Of Function

import random
import struct
import matplotlib.pyplot as plt


def show_plot():
    x = list()
    y = list()
    for i in range(0, len(population)):
        x.append(float(bin_to_float(population[i])))
    for i in range(0, len(population)):
        y.append(fitness(population[i]))
    fig, axes = plt.subplots(ncols=1, nrows=1, figsize=(5, 5))
    axes.set_title("Fitness /  Plot")
    plt.scatter(x, y)
    plt.show()


def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')


def bin_to_float(binary):
    return struct.unpack('!f', struct.pack('!I', int(binary, 2)))[0]


def get_equation_ans(y):
    x = float(bin_to_float(y))
    return float(eval(function))


def mutation():
    for i in range(0, len(population)):
        probability = random.randint(0, 100000)
        if probability < 10:
            print("Mutation Executed")
            genome = population[i]
            index = random.randint(0, 31)
            genome = genome[0:index] + str(random.randint(0, 1)) + genome[index + 1:len(genome)]
            while not (lower_bound <= float(bin_to_float(genome)) <= upper_bound):
                genome = population[i]
                index = random.randint(0, 32)
                genome = genome[0:index] + str(random.randint(0, 1)) + genome[index + 1:len(genome)]
            population[i] = genome


def crossover():
    children = list()
    for i in range(0, len(population) - 1, 2):
        index1 = -1
        index2 = -1
        probability = random.randint(1, 10)
        if probability <= 3:
            index1 = random.randint(0, int(len(population) / 2))
        else:
            index1 = random.randint(int(len(population) / 2), len(population) - 1)
        probability = random.randint(1, 10)
        if probability <= 3:
            index2 = random.randint(0, int(len(population) / 2))
        else:
            index2 = random.randint(int(len(population) / 2), len(population) - 1)
        genome1 = population[index1]
        genome2 = population[index2]
        index = random.randint(0, 31)
        child1 = genome1[0:index] + genome2[index:len(genome1)]
        child2 = genome2[0:index] + genome1[index:len(genome1)]
        while (not (lower_bound <= float(bin_to_float(child1)) <= upper_bound)) or (
                not (lower_bound <= float(bin_to_float(child1)) <= upper_bound)):
            index = random.randint(0, 31)
            child1 = genome1[0:index] + genome2[index:len(genome1)]
            child2 = genome2[0:index] + genome1[index:len(genome1)]
        children.append(child1)
        children.append(child2)
    for i in range(0, len(children)):
        population.append(children[i])


def selection():
    population.sort(key=fitness)
    size = int(len(population) / 2)
    for i in range(0, size):
        population.remove(population[0])


def fitness(genome):
    return -get_equation_ans(genome)


def generate_population():
    for i in range(0, genome_number):
        population.append(float_to_bin(random.random() * (upper_bound - lower_bound) + lower_bound))


function = input("Please Enter Your Function:")
lower_bound = float(input("Please Enter Your Lower Bound:"))
upper_bound = float(input("Please Enter Your Upper Bound:"))
generation_number = int(input("Please Enter Number Of Generations:"))
genome_number = int(input("Please Enter Number Of Genomes:"))
population = list()
generate_population()

for i in range(0, generation_number):
    show_plot()
    selection()
    crossover()
    mutation()

population.sort(key=fitness, reverse=True)
print(bin_to_float(population[0]))
