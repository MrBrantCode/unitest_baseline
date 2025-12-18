"""
QUESTION:
Write a function `largest_even_integer` that finds the largest even integer in a list of integers and returns a tuple containing the index position and the value of the largest even integer. The function should iterate through the list and keep track of the maximum even integer and its index position, updating them whenever it encounters a larger even integer. If no even integers are found, return (-1, -inf).
"""

def largest_even_integer(lst):
    max_num = float('-inf')
    max_index = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and lst[i] > max_num:
            max_num = lst[i]
            max_index = i
    return (max_index, max_num)