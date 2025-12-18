"""
QUESTION:
Function: exchange(lst1, lst2)

Given two lists of integers lst1 and lst2, determine if it's possible to swap elements between the two lists to make lst1 contain only even numbers while keeping the sum of elements in both lists the same. Return "YES" if possible, "NO" otherwise. Assume the input lists are not empty.
"""

def entrance(lst1, lst2):
    if (sum(lst1) + sum(lst2)) % 2 != 0:
        return "NO"
    lst1_odd = [i for i in lst1 if i%2 != 0]
    lst2_even = [i for i in lst2 if i%2 == 0]
    if not lst1_odd or not lst2_even:
        return "NO"
    diff = abs(sum(lst1) - sum(lst2))
    if diff % 2 != 0:
        return "NO"
    target = (diff // 2)
    lst1_odd_min = min(lst1_odd) if lst1_odd else float('inf')
    lst2_even_min = min(lst2_even) if lst2_even else float('inf')
    if sum(lst1) > sum(lst2):
        target = lst1_odd_min - lst2_even_min
    else:
        target = lst2_even_min - lst1_odd_min
    if target in set(lst1_odd) ^ set(lst2_even):
        return "YES"
    return "NO"