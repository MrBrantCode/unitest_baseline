"""
QUESTION:
Create a function called `multiply_lists` that takes two lists of numbers as input. The function should return a new list where each element is the product of the corresponding elements in the two input lists. If the input lists are not of the same length, the function should return an error message "Lists must have the same length".
"""

def multiply_lists(list1, list2):
    if len(list1) != len(list2):
        return "Lists must have the same length"
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])
    return result