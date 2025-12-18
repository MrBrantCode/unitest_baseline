"""
QUESTION:
Simulate the growth of a population of rabbits over a certain number of generations. Each pair of rabbits produces a litter of offspring, and these offspring take a certain amount of time to mature before they can reproduce. The population starts with one pair of immature rabbits, and rabbits never die. 

Write a function `total_rabbits(generations, litter_size, maturity_age)` that takes in three parameters: an integer representing the number of generations to simulate, an integer representing the number of offspring in each litter, and an integer representing the age at which rabbits become mature and can reproduce. 

The function should return the total number of rabbits after the specified number of generations.
"""

def total_rabbits(generations, litter_size, maturity_age):
    immature = 1
    mature = 0
    total = 1

    for _ in range(generations):
        new_immature = mature * litter_size  # Each mature pair produces a litter
        new_mature = immature  # Immature rabbits mature
        immature = new_immature
        mature += new_mature

        total = immature + mature  # Total rabbits at the end of the generation

    return total