"""
QUESTION:
Simulate the growth of a population over a specified number of generations. The population size increases based on a growth rate determined by the current population size and a fixed growth factor.

Create a function `simulate_population_growth(generations, growth_rate_percentage)` that takes two parameters:
- `generations`: an integer representing the number of generations to simulate
- `growth_rate_percentage`: a float representing the percentage growth rate for each generation

The function should return the final population size after simulating the specified number of generations, assuming an initial population size of 20 and rounding the result to 4 decimal places.
"""

def entance(generations, growth_rate_percentage):
    population = 20  
    for _ in range(generations):
        population += population * (growth_rate_percentage / 100)
    return round(population, 4)