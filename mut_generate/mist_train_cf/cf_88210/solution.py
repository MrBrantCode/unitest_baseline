"""
QUESTION:
Write a function `find_combinations(numbers, target)` that takes a list of integers and a target integer as input, and returns a list of all possible combinations of three integers from the input list where the sum of the three integers is equal to the target value. Each integer from the input list can only be used once in each combination. The function should also print the total number of combinations found and then print each combination in reverse order.
"""

from itertools import combinations

def find_combinations(numbers, target):
    """
    This function finds all possible combinations of three integers from the input list 
    where the sum of the three integers is equal to the target value.

    Args:
        numbers (list): A list of integers.
        target (int): The target sum.

    Returns:
        list: A list of combinations, where each combination is a list of three integers 
              in reverse order.
    """
    combinations_list = []
    
    for combination in combinations(numbers, 3):
        if sum(combination) == target:
            combinations_list.append(list(combination[::-1]))
    
    print("Total number of combinations:", len(combinations_list))
    for i, combination in enumerate(combinations_list):
        print("Combination", i+1, ":", combination)
    return combinations_list