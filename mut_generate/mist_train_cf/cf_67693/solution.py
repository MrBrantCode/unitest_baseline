"""
QUESTION:
Implement a Python function named `sum_xor`, `sum_and`, `sum_or`, and `sum_not` that compute the aggregate of xor, bitwise AND, and bitwise OR for every pair of numbers within a provided list, and the aggregate of the bitwise NOT operation for every number in the list, respectively. The functions should ensure each pair is counted only once and avoid pairing an element with itself. The bitwise NOT operation should be applied individually to each element, not in pairs.
"""

def sum_xor(lst):
    """Compute the aggregate of xor for every pair of numbers within a provided list."""
    total = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            total += lst[i] ^ lst[j]
    return total*2

def sum_and(lst):
    """Compute the aggregate of bitwise AND for every pair of numbers within a provided list."""
    total = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            total += lst[i] & lst[j]
    return total*2

def sum_or(lst):
    """Compute the aggregate of bitwise OR for every pair of numbers within a provided list."""
    total = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            total += lst[i] | lst[j]
    return total*2

def sum_not(lst):
    """Compute the aggregate of bitwise NOT for every number in the list."""
    total = 0
    for i in range(len(lst)):
        total += ~lst[i]
    return total