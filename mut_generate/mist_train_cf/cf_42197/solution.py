"""
QUESTION:
Create a function named `modify_numbers` that takes a list of integers and a boolean flag as input. If the flag is True, double all the even numbers in the list. If the flag is False, square all the odd numbers in the list. The function should return an empty list if the input list is empty. The function should not modify the original list.
"""

from typing import List

def modify_numbers(numbers: List[int], double_even: bool) -> List[int]:
    if not numbers:
        return []

    modified_numbers = []
    for num in numbers:
        if double_even:
            modified_numbers.append(num * 2 if num % 2 == 0 else num)
        else:
            modified_numbers.append(num ** 2 if num % 2 != 0 else num)
    return modified_numbers