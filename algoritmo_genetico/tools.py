import sys
from math import *

def binary_array_to_decimal(binary_array):
    binary_string = "".join(str(e) for e in binary_array)
    return int(binary_string, 2)

def print_population(population):
    i = 0
    for p in population:
        print("----------------------------------------------------------")
        print("| {:02d} | Apt: {} | Gene: {}".format(i, p.fitness_value, p.gene_value))
        i += 1

def print_phase_result(n, phase, population):
    print("================ [ FASE {}: {} ] ==================".format(n, phase))
    print_population(population)
    print("")

def print_best_subject(population, generation):
    min = inf
    best_subject = None

    for subject in population:
        if subject.fitness_value <= min:
            best_subject = subject
            min = subject.fitness_value

    print("================ [ Melhor da geracao: {} ] ================".format(generation))
    print("| Apt: {} | Gene: {}".format(best_subject.fitness_value, best_subject.gene_value))
    print("")

