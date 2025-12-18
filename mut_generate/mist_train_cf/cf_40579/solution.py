"""
QUESTION:
Write a function `is_palindrome(numero_list: List[int]) -> bool` that determines whether a given list of integers is a palindrome. The function should return `True` if the list is a palindrome and `False` otherwise. The input list will only contain integers and will be of length `n`.
"""

from typing import List

def entrance(numero_list: List[int]) -> bool:
    n = len(numero_list)
    for i in range(n // 2):
        if numero_list[i] != numero_list[n - i - 1]:
            return False
    return True