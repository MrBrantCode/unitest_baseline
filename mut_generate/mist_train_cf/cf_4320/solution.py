"""
QUESTION:
Write a function `sum_even_indices` that takes a list of integers as input and returns the sum of the even-indexed elements, ignoring any negative numbers and skipping over any duplicates. The function should only consider the first occurrence of each number and handle lists containing up to 10^6 elements with values ranging from -10^6 to 10^6.
"""

def sum_even_indices(lst):
    unique_lst = []
    for num in lst:
        if num >= 0 and num not in unique_lst:
            unique_lst.append(num)
    return sum(num for i, num in enumerate(unique_lst) if i % 2 == 0)