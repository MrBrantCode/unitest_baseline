"""
QUESTION:
Design a function named `sort_descending_order` that takes a list of integers as input and returns the list sorted in descending order. The function should implement the selection sort method and sort the list in-place without using any additional space. The function should not use built-in sort functions.
"""

def sort_descending_order(input_list):
    for i in range(len(input_list)):
        max_index = i
        for j in range(i+1, len(input_list)):
            if input_list[j] > input_list[max_index]:
                max_index = j
        if max_index != i:
            input_list[i], input_list[max_index] = input_list[max_index], input_list[i]
    return input_list