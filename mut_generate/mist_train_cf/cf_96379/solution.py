"""
QUESTION:
Create a function `remove_duplicates(arr)` that takes an array of at least 10,000 positive integers less than or equal to 100, removes all duplicate elements, counts the occurrence of each unique element, and returns the unique elements in descending order based on their count.
"""

from collections import Counter

def remove_duplicates(arr):
    # Remove duplicates and count the frequency of each element
    counter = Counter(arr)
    
    # Sort unique elements in descending order based on their count
    unique_elements = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    return unique_elements