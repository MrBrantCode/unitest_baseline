"""
QUESTION:
Create a function named `advanced_sort` that accepts a list `l`, an integer `n`, and a string `s`. The function should return a new list where elements at indices not divisible by `n` remain the same, and elements at indices divisible by `n` are replaced by their original index multiplied by 2 and then sorted in the order specified by `s` ('asc' for ascending or 'desc' for descending). The replacement should be done in the order of their appearance in the sorted list.
"""

def advanced_sort(l: list, n: int, s: str):
    divisible_indices = [i for i in range(len(l)) if (i + 1) % n == 0]
    divisible_elements = [i * 2 for i in range(len(l)) if (i + 1) % n == 0]
    sorted_elements = sorted(divisible_elements, reverse=(s == 'desc'))
    new_list = [l[i] if (i + 1) % n != 0 else sorted_elements.pop(0) for i in range(len(l))]
    return new_list