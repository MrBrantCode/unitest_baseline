"""
QUESTION:
Create a function that takes an unsorted list of integers as input, sorts it in ascending order without using built-in sorting functions, and removes any duplicates from the sorted list. The function should return the sorted list with no duplicates.
"""

def sort_and_remove_duplicates(input_list):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
    result = []
    for number in input_list:
        if number not in result:
            result.append(number)
    return result