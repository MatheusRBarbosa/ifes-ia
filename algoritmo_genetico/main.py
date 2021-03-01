from Subject import Subject
from Configs import Configs
from random import randint
from math import *
from tools import *

###########################
#          MAIN           #
###########################

def main():
    base_population = phase_create_population()
    selected_population = phase_tournament(base_population)
    crossovered_population = phase_crossover(selected_population)
    mutated_population = phase_mutation(crossovered_population)

###########################
#          PHASES         #
###########################

def phase_create_population():
    population = [Subject() for _ in range(configs.population_size[0])]
    print_phase_result(1, "População base", population)
    return population

def phase_tournament(population):
    size = configs.population_size[0]
    result_population = population

    for i in range(size):
        r1 = randint(0, size-1)
        r2 = randint(0, size-1)
        
        if(population[r1].fitness_value > population[r2].fitness_value):
            result_population[i] = population[r2]
        else:
            result_population[i] = population[r1]
    
    print_phase_result(2, "População selecionada", result_population)
    return result_population

def phase_crossover(population):
    size = configs.population_size[0]
    result_population = population

    for i in range(0, size, 2):
        r1 = randint(0, size-1)
        r2 = randint(0, size-1)

        can_crossover = randint(1, 100) <= configs.crossover_rate
        if(can_crossover):
            index_to_crop = randint(1, (configs.binary_gene_size - 1))

            actual = population[r1]
            next = population[r2]
            
            result_population[i] = actual.crossover(index_to_crop, next.binary_gene)
            result_population[i+1] = next.crossover(index_to_crop, actual.binary_gene)
    
    print_phase_result(3, "Crossover", result_population)
    return result_population

def phase_mutation(population):
    size = configs.population_size[0]
    result_population = population

    for subject in result_population:
        subject.mutate()
    
    return result_population


###########################
#         METHODS         #
###########################


global configs
configs = Configs()

main()