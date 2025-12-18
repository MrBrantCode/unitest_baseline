"""
QUESTION:
Write a function `perfectSquarePairs` that takes a list of integers as input and returns a boolean value. The function should return True if the input list has an even length and all pairs of adjacent elements are equal and are perfect squares, and False otherwise. The function should assume the input list has an even length. Note that the function may be subject to numerical precision issues for large numbers.
"""

def perfectSquarePairs(num_list):
    for i in range(0, len(num_list), 2):
        if num_list[i] != num_list[i+1] or round(num_list[i] ** 0.5) ** 2 != num_list[i]:
            return False
    return True