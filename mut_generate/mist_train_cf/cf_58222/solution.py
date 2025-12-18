"""
QUESTION:
Create a function `repeat_elements_in_list` that takes two inputs: an array `input_list` and a number `size`. The function should create a new array of the specified `size` by cycling through and copying elements from the original `input_list` sequentially, as many times as needed. If `size` is 0 or negative, return an empty list.
"""

def repeat_elements_in_list(input_list, size):
    if size <= 0:
        return []
    
    new_list = []
    for i in range(size):
        new_list.append(input_list[i % len(input_list)])
    return new_list