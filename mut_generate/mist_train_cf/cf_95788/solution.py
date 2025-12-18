"""
QUESTION:
Implement a function `abstract_method` that takes a list of integers as input and sorts the list in ascending order. The function should have a time complexity of O(n^2), where n is the length of the input list, and use only constant extra space. Additionally, the function should not use any built-in sorting functions or external libraries.
"""

def abstract_method(input_list):
    n = len(input_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if input_list[j] < input_list[min_idx]:
                min_idx = j
        input_list[i], input_list[min_idx] = input_list[min_idx], input_list[i]
    return input_list