"""
QUESTION:
Develop a function `find_unique_numbers` that takes a list of integers and an optional boolean parameter `desc` (defaulting to `False`) and returns a list of unique numbers in the input list. The list should be sorted in ascending order unless `desc` is `True`, in which case it should be sorted in descending order. The solution should achieve a time complexity better than O(n log n).
"""

from collections import Counter

def find_unique_numbers(arr, desc=False):
    frequency = Counter(arr)
    unique_elements = [key for key, value in frequency.items() if value == 1]
    unique_elements.sort(reverse=desc)
    
    return unique_elements