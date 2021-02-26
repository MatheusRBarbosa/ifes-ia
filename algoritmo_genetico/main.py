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

###########################
#          PHASES         #
###########################

def phase_create_population():
    population = [Subject() for _ in range(configs.population_size[0])]
    print_phase_result(1, "População base", population)
    return population

def phase_tournament(population):
    size = configs.population_size[0]
    result_population = [Subject() for _ in range(size)]

    #x = 0
    for i in range(size):
        r1 = randint(0, 9)
        r2 = randint(0, 9)
        
        #print("====> {}".format(x))
        #print("{}({}) vs {}({})".format(population[r1].fitness_value, r1, population[r2].fitness_value, r2))
        if(population[r1].fitness_value > population[r2].fitness_value):
            result_population[i] = population[r2]
        else:
            result_population[i] = population[r1]
        
        #x+=1
    
    print_phase_result(2, "População selecionada", result_population)
    return result_population

def phase_crossover(population):
    size = configs.population_size[0]
    result_population = [Subject() for _ in range(size)]

    for i in range(0, size, 2):
        r1 = randint(0, 9)
        r2 = randint(0, 9)

        can_crossover = randint(0, 100) <= configs.crossover_rate
        if(can_crossover):
            #TODO continue




###########################
#         METHODS         #
###########################


global configs
configs = Configs()

main()