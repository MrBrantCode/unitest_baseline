"""
QUESTION:
Create a function called `second_largest` that takes a list of integers as input and returns the second largest number in the list. The list may contain negative numbers, zeros, and duplicate values. The function should not use built-in sorting functions or methods. If all numbers in the list are the same, the function should return negative infinity.
"""

def second_largest(num_list):
    first_max = float('-inf')
    second_max = float('-inf')
    for i in range(len(num_list)):
        if (num_list[i] > first_max):
            second_max = first_max
            first_max = num_list[i]
        elif (num_list[i] > second_max and num_list[i] != first_max):
            second_max = num_list[i]
    return second_max