"""
QUESTION:
Implement the function `retrieve_unique_descending(lst: List[int]) -> List[int]` to retrieve unique values from a list of integers and return them in descending order. The input list contains 1 to 10^5 integers, each of which can be a negative or positive integer in the range -10^9 to 10^9.
"""

from typing import List

def retrieve_unique_descending(lst: List[int]) -> List[int]:
    return sorted(set(lst), reverse=True)