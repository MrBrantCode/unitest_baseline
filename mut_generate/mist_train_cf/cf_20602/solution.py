"""
QUESTION:
Write a function called "reverse_list" that takes a list as input and returns a new list with the elements in reverse order. The original list should remain unchanged. The time complexity of the function should be O(n), where n is the length of the input list. The function should not use any built-in reverse or slicing operations.
"""

def reverse_list(input_list):
    reversed_list = []
    for i in range(len(input_list)-1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list