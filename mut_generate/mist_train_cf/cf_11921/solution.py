"""
QUESTION:
Generate a function named `generate_unique_random_numbers` that takes two parameters, `start` and `end`, and returns a list of unique random numbers within the range specified by `start` and `end` (inclusive). The function should not use any built-in random number generation functions or libraries and should ensure that all numbers in the range are generated exactly once.
"""

def generate_unique_random_numbers(start, end):
    # Create a list of all numbers in the given range
    numbers = list(range(start, end+1))
    
    # Implement a simple Linear Congruential Generator (LCG) algorithm to generate a random index
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = 1
    for i in range(len(numbers) - 1, 0, -1):
        seed = (a * seed + c) % m
        j = seed % (i + 1)  # Generate a random index
        numbers[i], numbers[j] = numbers[j], numbers[i]  # Swap elements
        
    return numbers