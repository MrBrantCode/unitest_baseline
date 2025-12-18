"""
QUESTION:
Write a function named `sum_of_largest_three` that takes an unordered list of integers as input and returns the sum of the three largest integers in the list. The function should handle lists with less than three elements by returning the sum of all elements. The input list consists of only integers.
"""

def sum_of_largest_three(sequence):
    # Sort the sequence in descending order
    sequence.sort(reverse=True)
    
    # Sum the first three elements, which are the largest after sorting
    sum_of_largest = sum(sequence[:3])
    
    return sum_of_largest