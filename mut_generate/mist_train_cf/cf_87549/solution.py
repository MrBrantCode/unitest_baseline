"""
QUESTION:
Design a function named `multiply_list_elements` that takes two parameters, a list and a number. The function should return a list where all elements from the input list are multiplied by the absolute value of the given number. The input list should not contain any duplicate elements, can have a maximum length of 1000 elements, and can contain both integers and floats. If the input number is zero, the function should return an empty list.
"""

def multiply_list_elements(lst, num):
    if num == 0:
        return []
    
    return [element * abs(num) for element in lst]