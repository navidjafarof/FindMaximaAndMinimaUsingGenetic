# This is Code Trying to Find Minima and Maxima Of a Function in A Certain Range Using Genetic Algorithm
# Our Function is:
# X^3 * cos(x) + X^2 * cos(x) - X*sin(x)
# The Code Works For Both Minima And Maxima;
# If you Want to Find Maxima Your Fitness Function Must Return The Value Of Function
# Otherwise Your Fitness Function Must Return The -Value Of Function

import math
import random


def get_equation_ans(x):
    return x ** 3 * math.cos(x) + x ** 2 * math.cos(x) - x * math.sin(x)


def mutation(population_list):
    for i in range(0, len(population_list)):
        probability = random.randint(0, 100000)
        if probability < 10:
            print("Mutation Executed")
            gnome = str(population_list[i])
            index = random.randint(3, 19)
            gnome = float(str(gnome[0:index]) + str(random.randint(0, 10)) + str(gnome[index + 1:len(gnome)]))
            while not (-2 <= float(population_list[i]) <= 1):
                gnome = str(population_list[i])
                index = random.randint(0, len(gnome) - 2)
                gnome = float(str(gnome[0:index]) + str(random.randint(0, 10)) + str(gnome[index + 1:len(gnome)]))
            population_list[i] = float(gnome)


def crossover(population_list):
    children = list()
    for i in range(0, len(population_list), 2):
        genome1 = str(population_list[i])
        genome2 = str(population_list[len(population_list) - i - 1])
        child1 = -math.inf;
        child2 = child1;
        while (not (-2 <= float(child1) <= 1)) and (not (-2 <= float(child2) <= 1)):
            index = random.randint(3, 19)
            child1 = float(str(genome1[0:index]) + str(genome2[index:len(genome1)]))
            child2 = float(str(genome2[0:index]) + str(genome1[index:len(genome1)]))
        children.append(child1)
        children.append(child2)
    for i in range(0, len(children)):
        population_list.append(children[i])

    print(len(population_list))
    print(len(children))


def selection(population_list):
    population_list.sort(key=fitness)
    size = int(len(population_list) / 2)
    for i in range(0, size):
        population_list.remove(population_list[0])


def fitness(genome):
    return get_equation_ans(genome)


def create_population(population_list, number_of_genome, range_min, range_max):
    for i in range(0, number_of_genome):
        population_list.append(random.random() * (range_max - range_min) + range_min)


generation_number = int(input("Please Enter Number Of Generations:"))
genome_number = int(input("Please Enter Number Of Genomes:"))
population = list()
create_population(population, genome_number, -2, 1)

for i in range(0, generation_number):
    selection(population)
    crossover(population)
    mutation(population)

population.sort(key=fitness, reverse=True)
print(population[0])
