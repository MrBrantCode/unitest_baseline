"""
QUESTION:
Implement a function named `complex_operation` that takes a list of numbers as a parameter and modifies its elements by performing a complex mathematical operation. The operation should involve squaring each number, multiplying it by 2, and then subtracting 1. The function should return the modified list. Note that the function should modify the original list passed as a parameter, rather than creating a new list.
"""

def complex_operation(num_list):
    for i in range(len(num_list)):
        num_list[i] = (num_list[i] ** 2) * 2 - 1
    return num_list