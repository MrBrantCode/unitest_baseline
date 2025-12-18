"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as an input and returns a new list containing only the positive numbers from the input list, sorted in ascending order, with no duplicates. The function should not use any built-in sorting or duplicate removal functions.
"""

def get_positive_and_sort(numbers):
    def swap_elements(n, index1, index2):
        temp = n[index1]
        n[index1] = n[index2]
        n[index2] = temp

    positive_numbers = [num for num in numbers if num > 0]
    non_duplicates = []

    for num in positive_numbers:
        if num not in non_duplicates:
            non_duplicates.append(num)

    for i in range(len(non_duplicates)):
        for j in range(0, len(non_duplicates) - i - 1):
            if non_duplicates[j] > non_duplicates[j+1]:
                swap_elements(non_duplicates, j, j+1)

    return non_duplicates