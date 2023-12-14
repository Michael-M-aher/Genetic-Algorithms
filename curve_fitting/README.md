# Curve Fitting Genetic Algorithm

## Overview
This Python program implements a genetic algorithm to perform curve fitting, aiming to find the best coefficients for a polynomial equation that minimizes the distance between the curve and a given set of data points.

## Problem Description
Curve fitting involves constructing a mathematical function (polynomial equation) that best fits a series of data points. In this scenario, the goal is to use a genetic algorithm to find the optimal coefficients for the polynomial equation, minimizing the distance between the curve and the given data points.

## Input Format
The program reads input from a file with the following format:
- First line: Number of datasets (must be at least 1)
For each dataset:
- Number of data points and polynomial degree separated by space
For each point:
- x-coordinate and y-coordinate separated by space

Example:
```
1
4 2
1 5
2 8
3 13
4 20
```

## How to Run
1. Ensure you have Python installed.
1. Clone this repository to your local machine.
1. Navigate to the project directory in your terminal.
1. Place your input in curve_fitting_input.txt.
1. Run the program using the following command:
   ```bash
   python curve_fitting.py
   ```

## Output
The program outputs the best-fit coefficients for each testcase, along with the minimum distance achieved. The results are displayed in the console.

## Algorithm Description
The genetic algorithm involves evolving a population of candidate solutions over multiple generations. The program initializes a population, evaluates the fitness of each solution (coefficients), selects parents for reproduction, performs crossover and mutation, and repeats this process until convergence.

## Example Output
```
Test case 1:

Fitness: 0.8324661810613945
Genes: [3.163410770501011, 0.8095211080477718, 0.7269607606244115]
```

The output provides the coefficients of the polynomial equation that minimizes the distance for each dataset.