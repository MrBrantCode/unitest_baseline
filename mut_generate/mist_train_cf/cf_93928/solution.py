"""
QUESTION:
Create a function called `find_duplicates` that takes a list of integers as input and returns a list of integers that appear more than twice in the input list, in descending order. The input list can contain duplicate integers.
"""

from collections import Counter

def find_duplicates(arr):
    """
    This function takes a list of integers as input and returns a list of integers 
    that appear more than twice in the input list, in descending order.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    list: A list of integers that appear more than twice in the input list, in descending order.
    """
    
    # Count the occurrences of each element in the array
    counter = Counter(arr)
    
    # Find the duplicates that appear more than twice and sort them in descending order
    duplicates = sorted([key for key, value in counter.items() if value > 2], reverse=True)
    
    return duplicates