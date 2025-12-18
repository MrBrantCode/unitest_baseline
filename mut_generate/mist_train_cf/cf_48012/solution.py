"""
QUESTION:
Implement a function named `exchange(lst1, lst2)` that takes two lists of integers as input. The function should return "YES" if it is possible to swap elements between the lists such that `lst1` contains only even numbers and the total sum of elements in both lists remains equal. Otherwise, it should return "NO". Assume that the input lists are never empty.
"""

def exchange(lst1, lst2):
    sum1, sum2 = sum(lst1), sum(lst2)
    if (sum1 + sum2) % 2 == 1:
        return "NO"
    odd1 = min(i for i in lst1 if i % 2 == 1) if any(i % 2 == 1 for i in lst1) else float("inf")
    even2 = min(i for i in lst2 if i % 2 == 0) if any(i % 2 == 0 for i in lst2) else float("inf")
    if odd1 == float("inf") or even2 == float("inf") or odd1 > even2:
        return "NO"
    return "YES"