"""
QUESTION:
Write a function called `calculate_sum` that takes a list of numbers as input and returns the sum of its elements. If the sum is divisible by 2, the function should return the sum multiplied by 2; otherwise, it should return the sum divided by 2.
"""

def calculate_sum(input_list):
    sum_of_elements = sum(input_list)
    
    if sum_of_elements % 2 == 0:
        return sum_of_elements * 2
    else:
        return sum_of_elements / 2