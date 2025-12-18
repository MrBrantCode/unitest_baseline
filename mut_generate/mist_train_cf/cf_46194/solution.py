"""
QUESTION:
Write a function named `process_list` that takes a list of integers as input and performs the following operations: sorts the list in non-decreasing order without using any built-in sorting function, reverses the sorted list in-place, and removes all even numbers from the reversed list. Return the resulting list.
"""

def process_list(input_list):
    length = len(input_list)

    # Bubble sort
    for i in range(length):
        for j in range(0, length - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

    # Reverse
    i = 0
    j = length - 1
    while i < j:
        input_list[i], input_list[j] = input_list[j], input_list[i]
        i += 1
        j -= 1

    # Remove even numbers
    i = 0
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            input_list.pop(i)
        else:
            i += 1

    return input_list