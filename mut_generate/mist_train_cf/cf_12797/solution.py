"""
QUESTION:
Create a function called `multiply_list_elements` that takes a list of positive integers as input and returns their product without using the '*' operator or any built-in multiplication functions. The function should only use addition, subtraction, and bit shifting operations.
"""

def multiply_list_elements(lst):
    result = 1
    for num in lst:
        partial_result = 0
        for _ in range(num):
            partial_result += 1
        temp_result = 0
        for _ in range(partial_result):
            temp_result += result
        result = temp_result
    return result