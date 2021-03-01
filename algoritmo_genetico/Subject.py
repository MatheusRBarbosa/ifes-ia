from random import randint
from Configs import Configs
from tools import *
from math import *

class Subject():
    def __init__(self):
        self.configs = Configs()
        self.binary_gene = []
        self.gene_value = 0
        self.fitness_value = 0
        self.__init_values()
    
    def crossover(self, index, parent):
        child = Subject()
        child.binary_gene[:index] = self.binary_gene.copy()
        child.binary_gene[index:] = parent[index:].copy()
        child.gene_value = self.__generate_gene_value()

        return child
    
    def mutate(self):
        for i in range(len(self.binary_gene)):
            can_mutate = randint(1, 100) <= self.configs.mutate_rate
            if(can_mutate):
                if self.binary_gene[i] == 0:
                    self.binary_gene[i] = 1
                else:
                    self.binary_gene[i] = 0

    def __normalize_gene_value(self, value):
        min = self.configs.normalized_interval[0]
        max = self.configs.normalized_interval[1]
        
        #TODO: X nao pode estar fora do intervalo de -20 a 20. Revisar logica
        x = min + (((max - min) * value) / (2**self.configs.binary_gene_size - 1))
        return x
    
    def __generate_binary_gene(self):
        binary_gene = [randint(0, 1) for _ in range(self.configs.binary_gene_size)]
        return binary_gene

    def __generate_gene_value(self):
        decimal_value = binary_array_to_decimal(self.binary_gene)
        normalized_value = self.__normalize_gene_value(decimal_value)
        return normalized_value
    
    def __fitness_function(self):
        fitness_value = cos(self.gene_value) * self.gene_value + 2
        return fitness_value

    def __init_values(self):
        self.binary_gene = self.__generate_binary_gene()
        self.gene_value = self.__generate_gene_value()
        self.fitness_value = self.__fitness_function()     
    