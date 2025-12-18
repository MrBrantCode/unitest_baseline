"""
QUESTION:
Implement a function `complex_operation` that takes a list of numbers as a reference parameter and modifies the original list by performing the mathematical operation `(num ** 2) + (2 * num) - 1` on each element. The function should return the modified list. Note that the input list is passed by reference, and any changes made to the list within the function should affect the original list.
"""

def complex_operation(num_list):
    # Perform a complex mathematical operation on the input list
    for i in range(len(num_list)):
        num_list[i] = (num_list[i] ** 2) + (2 * num_list[i]) - 1

    # Return the modified list
    return num_list