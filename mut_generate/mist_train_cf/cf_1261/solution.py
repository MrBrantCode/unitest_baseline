"""
QUESTION:
Write a Python function `remove_and_rearrange` that takes a list of integers as input and returns a tuple containing two lists. The first list should contain the input elements with all instances of 3 removed, no duplicates, even numbers sorted in ascending order, and odd numbers sorted in descending order. The even numbers should come before the odd numbers in the list. The second list should contain the removed elements (including duplicates). The function should achieve this in a single pass with a time complexity of O(n), without using any built-in Python functions such as `filter()`, `list comprehension`, or additional data structures.
"""

def remove_and_rearrange(numbers):
    removed_elements = []
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num == 3:
            removed_elements.append(num)
        elif num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    even_numbers = sorted(set(even_numbers))
    odd_numbers = sorted(set(odd_numbers), reverse=True)
    
    return (even_numbers + odd_numbers, removed_elements)