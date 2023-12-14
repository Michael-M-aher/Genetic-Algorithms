import random
from typing import List
import numpy as np


POPULATION_SIZE = 6
CROSSOVER_PROBABILITY = .7 #.4 to → .7
MUTATION_PROBABILITY = .1 #0.001 → 0.1
MAX_GENERATIONS = 50

x_points = np.array([])
y_points = np.array([])
d = 0

class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self._calc_fitness(self.genes)
        self.length = len(self.genes)

    def _calc_fitness(self, genes):
        fitness = 0
        for i in range (0,len(x_points)):
            tmp = 0 
            for j in range(0,len(genes)):
                tmp += genes[j]*(pow(x_points[i],j))
            tmp-=y_points[i]
            tmp = pow(tmp,2)
            tmp = round(tmp,3)
            fitness +=tmp
            fitness = round(fitness,3)
        fitness = fitness/len(x_points)
        return 1/fitness 
    def get_genes(self):
        return self.genes
    
    # def __repr__(self):
    #     return f''
    
    def __str__(self):
        return f'Fitness: {self.fitness}\nGenes: {self.genes}\n\n'
    
def initialize_population():
    return [Chromosome([random.uniform(-10,10) for _ in range(d+1)]) for _ in range(POPULATION_SIZE)]

def select_tournament(population):
    tournament = random.sample(population, 2)
    if tournament[0].fitness > tournament[1].fitness:
        return tournament[0]
    else:
        return tournament[1]
    

def crossover_two_point(parent1, parent2):
    crossover_point1 = random.randint(0, parent1.length-1)
    crossover_point2 = random.randint(0, parent1.length-1)
    while crossover_point1 == crossover_point2:
        crossover_point2 = random.randint(0, parent1.length-1)
    if crossover_point1 > crossover_point2:
        crossover_point1, crossover_point2 = crossover_point2, crossover_point1
    new_g1 = parent1.get_genes()[:crossover_point1] + parent2.get_genes()[crossover_point1:crossover_point2] + parent1.get_genes()[crossover_point2:]
    new_g2 = parent2.get_genes()[:crossover_point1] + parent1.get_genes()[crossover_point1:crossover_point2] + parent2.get_genes()[crossover_point2:]
    return Chromosome(new_g1), Chromosome(new_g2)

def mutate(chromosome,generation_number):
    genes = chromosome.get_genes()
    for i in range(chromosome.length):
        r = random.random()
        if r < MUTATION_PROBABILITY:
            genes[i] = mutate_gene(genes[i],generation_number)
    return Chromosome(genes)
    
def mutate_gene(gene,t):
    lower = gene - (-10)
    upper = 10 - gene
    r = random.random()
    if r <= 0.5:
        delta = lower * (1 - random.random() ** ((1 - t/MAX_GENERATIONS)**1))
        return gene - delta
    else:
        delta = upper * (1 - random.random() ** ((1 - t/MAX_GENERATIONS)**1))
        return gene + delta



def genetic_algorithm():
    generation_number = 0

    population = initialize_population()
       
    with open('curve_fitting_output.txt', 'a') as file:
        # print(f'Generation: {generation_number}\n{population[0]}\n\n')
        file.write(f'Generation: {generation_number}\n{population[0]}\n\n')
        while generation_number < MAX_GENERATIONS:

            generation_number += 1

            # SELECTION
            selected1 = select_tournament(population)
            selected2 = select_tournament(population)

            # CROSSOVER
            crossed_offspring = []
            r = random.random()
            if r < CROSSOVER_PROBABILITY:
                kid1, kid2 = crossover_two_point(selected1, selected2)
                crossed_offspring.append(kid1)
                crossed_offspring.append(kid2)
            else:
                crossed_offspring.append(selected1)
                crossed_offspring.append(selected2)
                
            # MUTATION
            for mutant in crossed_offspring:
                new_mutant = mutate(mutant,generation_number)
                population.append(new_mutant)
            
            # REPLACEMENT
            population = sorted(population, key=lambda ind: ind.fitness, reverse=True)
            population = population[:POPULATION_SIZE]

            # print(f'Generation: {generation_number}\n{population[0]}\n\n')
            file.write(f'Generation: {generation_number}\n{population[0]}\n\n')

        file.write(f'\nBest solution: {population[0]}\n\n\n')
        file.close()
    print(f'{population[0]}\n')


with open('curve_fitting_input.txt', 'r') as file, open('curve_fitting_output.txt', 'w') as of:
    of.close()
    test_cases = int(file.readline())
    for i in range(test_cases):
        print(f'Test case {i+1}:\n')
        with open('curve_fitting_output.txt', 'a') as o:
            o.write(f'Test case {i+1}:\n\n')
            o.close()
        n, d = map(int, file.readline().split()) 
        x_points = np.array([])
        y_points = np.array([])
        for j in range(n): 
            x, y = map(float, file.readline().split())
            x_points = np.append(x_points, x)
            y_points = np.append(y_points, y)

        genetic_algorithm()
    file.close()