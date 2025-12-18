"""
QUESTION:
Create a function `reverse_list` that takes a list of elements as input and reverses the order of its elements in-place without using any built-in reverse methods, slicing, or additional lists for storage. The function should modify the original list and return the reversed list.
"""

def reverse_list(input_list):
    start = 0
    end = len(input_list) - 1

    while start < end:
        input_list[start], input_list[end] = input_list[end], input_list[start]
        start += 1
        end -= 1

    return input_list