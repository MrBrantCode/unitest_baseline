"""
QUESTION:
Create a function `split_list` that takes a list of integers as input and returns a tuple of two lists: one containing the odd numbers and the other containing the even numbers. The odd and even numbers should maintain their relative order from the original list. If there are no odd numbers or no even numbers in the list, return an empty list for the corresponding part. The function should have a time complexity of O(n), where n is the length of the input list.
"""

from typing import List, Tuple

def split_list(lst: List[int]) -> Tuple[List[int], List[int]]:
    odd_numbers = []
    even_numbers = []
    
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return odd_numbers, even_numbers