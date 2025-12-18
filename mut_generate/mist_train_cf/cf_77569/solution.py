"""
QUESTION:
Create a function custom_sort(l: list, n: int, m: int, s: str) that accepts a list l, two integers n and m, and a sorting order s ('asc' or 'desc'). The function should return a new list that matches the original list l at indices not in range(n, m), while its values at indices in range(n, m) are equal to the corresponding indices of l raised to the power of 2, and sorted in the specified order s.
"""

def custom_sort(l: list, n: int, m: int, s: str):
    to_sort = [x**2 for x in l[n:m]]
    sorted_to_sort = sorted(to_sort, reverse=(s == 'desc'))
    return l[:n] + sorted_to_sort + l[m:]