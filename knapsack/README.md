# Knapsack Genetic Algorithm

## Overview
This Python program implements a genetic algorithm to solve the classic knapsack problem. The knapsack problem involves maximizing the total value of selected items to be placed in a knapsack, considering the weight capacity of the knapsack.

## Problem Description
The knapsack problem is a well-known optimization problem. Given a knapsack with a weight limit and a set of items, each with a weight and a value, the goal is to select the items to maximize the total value within the weight limit of the knapsack.

## Input Format
The program reads input from a file with the following format:
- First line: Number of test cases (must be at least 1)
For each test case:
- Size of the knapsack
- Number of items
For each item:
- Weight and value separated by space

Example:
```
2

14
5
4 1
7 7
1 22
3 23
3 6

28
5
10 27
9 27
8 12
8 28
3 23
```

## How to Run
1. Ensure you have Python installed.
1. Clone this repository to your local machine.
1. Navigate to the project directory in your terminal.
1. Place your input in knapsack_input.txt.
1. Run the program using the following command:
   ```bash
   python knapsack.py
   ```

Output
The program outputs the selected items for each test case along with the total value achieved. The results are displayed in the console.

Algorithm Description
The genetic algorithm involves evolving a population of candidate solutions over multiple generations. The program initializes a population, evaluates the fitness of each solution, selects parents for reproduction, performs crossover and mutation, and repeats this process until convergence.

Example Output
```
Test case 1:

Number of selected items: 4
Total Weight: 14
Total Value: 58
Chromosome: [0, 1, 1, 1, 1]
Items: [(7, 7), (1, 22), (3, 23), (3, 6)]

Test case 2:

Number of selected items: 4
Total Weight: 28
Total Value: 90
Chromosome: [0, 1, 1, 1, 1]
Items: [(9, 27), (8, 12), (8, 28), (3, 23)]
```