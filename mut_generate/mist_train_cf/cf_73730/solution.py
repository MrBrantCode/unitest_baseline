"""
QUESTION:
Create a function `future_flight(q, w)` that takes a sequence `q` and a weight `w` as inputs. The function should return `True` if `q` is a palindrome, its elements are sorted in either ascending or descending order, and the sum of its elements does not exceed `w`. The function should return `False` otherwise. If `q` is not a sequence, return "Non-sequence input". If `q` contains non-numeric elements, return "Non-numeric input". If `q` is not sorted in either ascending or descending order, return "Unsorted list error".
"""

def future_flight(q, w):
    if not isinstance(q, (list, tuple)):
        return "Non-sequence input"
    if not all(isinstance(item, (int, float)) for item in q):
        return "Non-numeric input"
    if q != sorted(q) and q != sorted(q, reverse=True):
        return "Unsorted list error"
    return q == q[::-1] and sum(q) <= w