"""
QUESTION:
Implement a function `split_list` that takes a list of unique integers as input and splits it into two parts: one part containing odd numbers and the other part containing even numbers. The odd numbers and even numbers should maintain their relative order. If there are no odd numbers or no even numbers in the list, return an empty list for the corresponding part. The function should have a time complexity of O(n), where n is the length of the input list.
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