"""
QUESTION:
Implement a function named `sum_unique_integers` that takes a list of numbers as input, including integers and floats, and returns the sum of all unique numbers in the list. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def sum_unique_integers(lst):
    unique_numbers = set()
    total_sum = 0
    
    for num in lst:
        if num not in unique_numbers:
            unique_numbers.add(num)
            total_sum += num
    
    return total_sum