"""
QUESTION:
Write a function named `find_indices` that takes a list of numbers as input and returns a list of indices of the second smallest even value in the list. The list of indices should include all occurrences of the second smallest even value. If the second smallest even value appears only once, return a list with a single index. If the list contains less than two distinct even numbers, return an empty list or the list of indices of the smallest even number.
"""

def find_indices(lst):
    evens = sorted(set([num for num in lst if num % 2 == 0]))
    
    if len(evens) < 2:
        return []
    
    second_smallest_even = evens[1]
    return [i for i, num in enumerate(lst) if num == second_smallest_even]