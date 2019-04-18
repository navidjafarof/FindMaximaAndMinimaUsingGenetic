# X^3 * cos(x) + X^2 * cos(x) - X*sin(x) minima and maxima
import math
import random


def get_equation_ans(x):
    return x ** 3 * math.cos(x) + x ** 2 * math.cos(x) - x * math.sin(x)


def mutation(population_list):
    for i in range(0, len(population_list)):
        probability = random.randint(0, 100000)
        print(probability)
        if probability < 10:
            print("mutation")
            gnome = str(population_list[i])
            index = random.randint(3, 19)
            gnome = float(str(gnome[0:index]) + str(random.randint(0, 10)) + str(gnome[index + 1:len(gnome)]))
            while not (-2 <= float(population_list[i]) <= 1):
                gnome = str(population_list[i])
                index = random.randint(0, len(gnome) - 2)
                gnome = float(str(gnome[0:index]) + str(random.randint(0, 10)) + str(gnome[index + 1:len(gnome)]))
            population_list[i] = float(gnome)


def crossover(population_list):
    for i in range(0, int(len(population_list) / 2)):
        gnome1 = str(population_list[i])
        gnome2 = str(population_list[len(population_list) - i - 1])
        child1 = -math.inf;
        child2 = child1;
        while (not (-2 <= float(child1) <= 1)) and (not (-2 <= float(child2) <= 1)):
            index = random.randint(3, 19)
            child1 = float(str(gnome1[0:index]) + str(gnome2[index:len(gnome1)]))
            child2 = float(str(gnome2[0:index]) + str(gnome1[index:len(gnome1)]))
        population_list.append(child1)
        population_list.append(child2)


def selection(population_list):
    population_list.sort(key=fitness)
    for i in range(0, int(len(population_list) / 2)):
        population_list.remove(population_list[0])


def fitness(genome):
    return get_equation_ans(genome)


def create_population(population_list, number, range_min, range_max):
    for i in range(0, number):
        population_list.append(random.random() * (range_max - range_min) + range_min)


population = list()
create_population(population, 1000, -2, 1)
generation_number = int(input("Please Enter Number Of Generations:"))

for i in range(0, generation_number):
    selection(population)
    crossover(population)
    mutation(population)

population.sort(key=fitness, reverse=True)
print(population[0])
