"""
QUESTION:
Write a function called `flatten_divisible_by_two_and_three` that takes a list of lists of integers as input and returns a new list containing all integers from the input that are divisible by both 2 and 3. The function should flatten the input list, meaning it should return a one-dimensional list of integers.
"""

def flatten_divisible_by_two_and_three(lst):
    flattened_list = []
    for sublist in lst:
        for num in sublist:
            if num % 2 == 0 and num % 3 == 0:
                flattened_list.append(num)
    return flattened_list