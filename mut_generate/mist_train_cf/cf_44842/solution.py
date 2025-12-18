"""
QUESTION:
Create a function named `reverse_reciprocal` that takes a list of numbers as input and returns a new list containing the reciprocal of each number in the original list order. The function should handle the case where the input list contains a zero, which would cause a division by zero error when calculating the reciprocal. The function should not modify the original list.
"""

def reverse_reciprocal(array):
    new_list = []
    for i in range(len(array) - 1, -1, -1):  
        try:
            new_list.append(1/array[i])
        except ZeroDivisionError:
            print("Error: Divided by zero!")  
    new_list.reverse()  
    return new_list