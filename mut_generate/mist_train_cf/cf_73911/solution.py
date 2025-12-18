"""
QUESTION:
Create a function named `binary_ones_desc_sorter` that takes a list of positive integers as input and returns the sorted list. The list should be sorted first by the count of 1s in the binary representation of each number in ascending order, and in case of a tie, the numbers should be sorted in descending order of their numerical values.
"""

def binary_ones_desc_sorter(input_list):
    input_list.sort(reverse=True)
    return sorted(input_list, key=lambda x: bin(x).count('1'))