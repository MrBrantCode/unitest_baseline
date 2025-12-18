"""
QUESTION:
Write a function `divide_list` that takes a list of integers as input, divides it into two halves, and returns both halves. If the list has an odd number of elements, place the middle element in the second half. The function must not use any built-in list splitting functions.
"""

def divide_list(input_list):
    mid = len(input_list) // 2
    if len(input_list) % 2 != 0:
        mid += 1
    first_half = [input_list[i] for i in range(0, mid)]
    second_half = [input_list[i] for i in range(mid, len(input_list))]
    return first_half, second_half