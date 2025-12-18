"""
QUESTION:
Design a function `will_it_fly` that determines if an array of integers `q` can "fly". For `q` to "fly", it must satisfy the following conditions: 
1. `q` must be a palindrome.
2. The sum of the elements in `q` must be less than or equal to the maximum allowed weight `w`.
3. `q` must contain exactly `n` unique elements.
The function should be optimized for efficiency with large arrays.
"""

def will_it_fly(q, w, n):
    # Check if q is palindromic
    if q != q[::-1]:
        return False

    # Check if the sum of elements in q is less than or equal to w
    if sum(q) > w:
        return False

    # Count the unique elements in q
    unique_elements = len(set(q))

    # Check if q has exactly n unique elements
    if unique_elements != n:
        return False

    return True