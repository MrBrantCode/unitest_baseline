"""
QUESTION:
Write a function `genetic_algorithm_stats` that takes in the following parameters: 
- `generations`: A list of dictionaries representing the individuals in each generation.
- `population_size`: An integer representing the size of the population.
- `elitism_proportion`: A float representing the proportion of individuals to be preserved through elitism.
- `mutation_probability`: A float representing the probability of mutation for an individual.
- `mutation_std_deviation`: A float representing the standard deviation for mutation.

The function should return a string in the following format:
```
Generation: 0
key1: value1
key2: value2
...

Population size: <population_size>
Elitism Proportion: <elitism_proportion>
Mutation Probability: <mutation_probability>
Mutation Std Deviation: <mutation_std_deviation>
```
Where `<population_size>`, `<elitism_proportion>`, `<mutation_probability>`, and `<mutation_std_deviation>` are replaced with the actual values.
"""

def genetic_algorithm_stats(generations, population_size, elitism_proportion, mutation_probability, mutation_std_deviation):
    stats_str = ""
    for i, gen in enumerate(generations):
        stats_str += f"Generation: {i}\n"
        for key, value in gen.items():
            stats_str += f"{key}: {value}\n"
    
    stats_str += f"\nPopulation size: {population_size}\n"
    stats_str += f"Elitism Proportion: {elitism_proportion}\n"
    stats_str += f"Mutation Probability: {mutation_probability}\n"
    stats_str += f"Mutation Std Deviation: {mutation_std_deviation}\n"
    
    return stats_str