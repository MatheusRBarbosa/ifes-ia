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
            
    def __normalize_gene_value(self, value):
        min = self.configs.normalized_interval[0]
        max = self.configs.normalized_interval[1]
        
        #TODO: X nao pode estar fora do intervalo de -20 a 20. Revisar logica
        x = min + (((max - min) * value) / (2**self.configs.subject_size - 1))
        return x
    
    def __generate_gene_value(self):
        binary_gene = [randint(0, 1) for _ in range(self.configs.subject_size)]
        self.binary_gene = binary_gene

        decimal_value = binary_array_to_decimal(binary_gene)
        normalized_value = self.__normalize_gene_value(decimal_value)
        
        return normalized_value
    
    def __fitness_function(self):
        fitness_value = cos(self.gene_value) * self.gene_value + 2
        return fitness_value

    def __init_values(self):
        self.gene_value = self.__generate_gene_value()
        self.fitness_value = self.__fitness_function()     
    