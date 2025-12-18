"""
QUESTION:
Create a function named `store_combinations` that generates all combinations of numbers from 1 to 10 using nested for loops, where the inner loop starts from the current number of the outer loop. Store these combinations in a suitable data structure with the combination as the key and any value. The function should also be able to retrieve and return a specific combination based on the input. The key should be in the format 'X-Y' where X and Y are the numbers in the combination.
"""

def store_combinations(combination=None):
    combinations = {}
    for i in range(1, 11):
        for j in range(i, 11):
            key = f"{i}-{j}"
            combinations[key] = True
    if combination:
        return combinations.get(combination)
    return combinations