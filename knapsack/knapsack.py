import random
from typing import List
import numpy as np


POPULATION_SIZE = 6
CROSSOVER_PROBABILITY = .7 #.4 to → .7
MUTATION_PROBABILITY = .1 #0.001 → 0.1
MAX_GENERATIONS = 50

items = []
knapsize = 0

class Chromosome:
    def __init__(self, genes: List[int]):
        self.genes = genes
        self.fitness = self._calc_fitness(self.genes)
        self.weight = self._calc_weight(self.genes)
        self.num_selected = sum(self.genes)

    def _calc_fitness(self, genes):
        fitness = 0
        weight = 0
        for i, gene in enumerate(genes):
            fitness += gene * items[i][1]
            weight += gene * items[i][0]
        if weight > knapsize:
            fitness = 0
        return fitness
    
    def _calc_weight(self, genes):
        weight = 0
        for i, gene in enumerate(genes):
            weight += gene * items[i][0]
        return weight
    
    def get_genes(self):
        return self.genes
    
    def __repr__(self):
        return f'Number of selected items: {self.num_selected}\nTotal Weight: {self.weight}\nTotal Value: {self.fitness}\nChromosome: {self.genes}\nItems: {[items[i] for i, gene in enumerate(self.genes) if gene == 1]}'
    
    def __str__(self):
        return f'Number of selected items: {self.num_selected}\nTotal Weight: {self.weight}\nTotal Value: {self.fitness}\nChromosome: {self.genes}\nItems: {[items[i] for i, gene in enumerate(self.genes) if gene == 1]}'
    
def initialize_population():
    return [Chromosome([random.randint(0,1) for _ in range(len(items))]) for _ in range(POPULATION_SIZE)]

def select_rank(population):
    sorted_population = sorted(population, key=lambda ind: ind.fitness, reverse=True)
    size = len(sorted_population)
    sum_rank = (size * (size + 1)) / 2
    propabilities = [i/sum_rank for i in range(1, size+1)]
    cummulative_propabilities = np.cumsum(propabilities)
    selected = None
    r = random.random()
    for i in range(size):
        if r < cummulative_propabilities[i]:
            selected = sorted_population[i]
            break
    return selected
    

def crossover_one_point(parent1, parent2):
    crossover_point = random.randint(0, len(parent1.get_genes())-1)
    new_g1 = parent1.get_genes()[:crossover_point] + parent2.get_genes()[crossover_point:]
    new_g2 = parent2.get_genes()[:crossover_point] + parent1.get_genes()[crossover_point:]
    return Chromosome(new_g1), Chromosome(new_g2)

def mutate(chromosome):
    mutated_genes = chromosome.get_genes().copy()
    for i in range(len(mutated_genes)):
        if random.random() < MUTATION_PROBABILITY:
            mutated_genes[i] = mutate_gene(mutated_genes[i])
    return Chromosome(mutated_genes)
    
def mutate_gene(gene):
    return 1 if gene == 0 else 0


def genetic_algorithm():
    generation_number = 0

    population = initialize_population()
       
    with open('knapsack_output.txt', 'a') as file:
        # print(f'Generation: {generation_number}\n{population[0]}\n\n')
        file.write(f'Generation: {generation_number}\n{population[0]}\n\n')
        while generation_number < MAX_GENERATIONS:

            generation_number += 1

            # SELECTION
            selected1 = select_rank(population)
            selected2 = select_rank(population)

            # CROSSOVER
            crossed_offspring = []
            if random.random() < CROSSOVER_PROBABILITY:
                kid1, kid2 = crossover_one_point(selected1, selected2)
                crossed_offspring.append(kid1)
                crossed_offspring.append(kid2)
            else:
                crossed_offspring.append(selected1)
                crossed_offspring.append(selected2)
                
            # MUTATION
            for mutant in crossed_offspring:
                new_mutant = mutate(mutant)
                population.append(new_mutant)
            
            # REPLACEMENT
            population = sorted(population, key=lambda ind: ind.fitness, reverse=True)
            population = population[:POPULATION_SIZE]

            # print(f'Generation: {generation_number}\n{population[0]}\n\n')
            file.write(f'Generation: {generation_number}\n{population[0]}\n\n')

        file.write(f'\nBest solution: {population[0]}\n\n\n')
        file.close()
    print(f'{population[0]}\n')


with open('knapsack_input.txt', 'r') as file, open('knapsack_output.txt', 'w') as of:
    of.close()
    test_cases = int(file.readline())
    for i in range(test_cases):
        print(f'Test case {i+1}:\n')
        with open('knapsack_output.txt', 'a') as o:
            o.write(f'Test case {i+1}:\n\n')
            o.close()
        inp = file.readline()
        while inp == '\n':
            inp = file.readline()
        knapsize = int(inp)
        inp = file.readline()
        num_items = int(inp) 
        items = [] 
        for j in range(num_items): 
            weight, value = map(int, file.readline().split()) 
            items.append((weight, value)) 
        genetic_algorithm()
    file.close()