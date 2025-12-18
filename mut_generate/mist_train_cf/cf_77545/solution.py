"""
QUESTION:
Create a Python function `is_sorted` that takes a list of integers as input and returns `True` if the list is sorted in non-decreasing order based on their digital roots, and `False` otherwise. The digital root of a number is the recursive sum of its digits until a single-digit number is produced, with the assumption that the digital root of 0 is 0.
"""

def is_sorted(lst):
    def digital_root(n):
        return (n - 1) % 9 + 1 if n > 0 else 0

    digital_roots = [digital_root(num) for num in lst]
    return all(digital_roots[i] <= digital_roots[i + 1] for i in range(len(digital_roots) - 1))