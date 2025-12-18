"""
QUESTION:
Create a function `stable_flight(q, w, k)` that takes a list `q` and two integers `w` and `k` as input. The function should return `True` if the list `q` is palindromic, the sum of its elements is less than or equal to `w`, and no element in the list exceeds `k`. Otherwise, it should return `False`.
"""

def stable_flight(q, w, k):
    # Check if q is palindromic
    if q != q[::-1]:
        return False
    # Check if sum of q is within the permissible weight
    if sum(q) > w:
        return False
    # Check if any of the elements exceed the individual limit, k
    if any(i > k for i in q):
        return False
    return True