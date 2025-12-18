"""
QUESTION:
Create a function `will_it_fly` that takes a list of integers `q`, an integer `w`, and an integer `n` as input. The function should return `True` if `q` is a palindrome, the sum of its elements is less than or equal to `w`, and it contains exactly `n` smallest unique digits. Otherwise, it should return `False`. The function should be efficient for large lists.
"""

def will_it_fly(q, w, n):
    # Check if the list is a palindrome.
    if q != q[::-1]:
        return False

    # Check if the sum of numbers is less than or equal to w.
    if sum(q) > w:
        return False
    
    # Check if the size of unique smallest numbers is equal to n.
    if len(set(sorted(q)[:n])) != n:
        return False
    
    return True