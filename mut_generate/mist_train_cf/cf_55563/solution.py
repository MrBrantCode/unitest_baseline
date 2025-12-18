"""
QUESTION:
Create a function called `will_it_fly(q, w)` that takes two parameters: a list of integers `q` and an integer `w`. The function should return `True` if the list `q` is palindromic and the sum of its elements is less than or equal to `w`. Otherwise, it should return `False`. The function should be optimized to handle large lists efficiently.
"""

def will_it_fly(q, w):
    q_len = len(q)
    
    # Check if the list is palindromic
    for i in range(q_len // 2):
        if q[i] != q[q_len - 1 - i]:
            return False
    
    # Check if the sum of its elements is less than or equal to w
    if sum(q) > w:
        return False
    
    return True