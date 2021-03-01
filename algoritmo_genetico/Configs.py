class Configs:
    def __init__(self):
        self.binary_gene_size = 16
        self.normalized_interval = [-20, 20]
        self.population_size = [10, 20]
        self.crossover_rate = 60
        self.mutate_rate = 1

    #TODO: fazer um get para population size baseado em args. Dessa forma sera possivel testar tamanhos diferentes mais facilmente