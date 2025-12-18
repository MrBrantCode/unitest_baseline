"""
QUESTION:
Write a function `find_three_elements` that takes an array and a target number as input. The function should return the first combination of three even numbers from the array that sum up to the target number. Each number in the array can only be used once, and the order of the numbers in the output does not matter. If no such combination exists, the function should return `None`.
"""

from itertools import combinations

def find_three_elements(arr, target):
    for comb in combinations(arr, 3):
        if sum(comb) == target and all(el % 2 == 0 for el in comb):
            return comb
    return None