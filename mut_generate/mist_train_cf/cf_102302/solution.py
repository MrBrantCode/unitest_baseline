"""
QUESTION:
Write a function `find_largest_even_integer` that takes a list of integers as input and returns a tuple containing the index and value of the largest even integer in the list. If there are multiple even integers with the same maximum value, return the index and value of the first occurrence. The function should handle lists containing duplicates.
"""

def find_largest_even_integer(lst):
    max_num = float("-inf")
    max_index = -1
    for i, num in enumerate(lst):
        if num % 2 == 0:
            if num > max_num:
                max_num = num
                max_index = i
            elif num == max_num:
                max_index = min(max_index, i)
    if max_index == -1:
        return None
    else:
        return (max_index, max_num)