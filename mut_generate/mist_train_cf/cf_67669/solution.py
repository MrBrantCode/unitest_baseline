"""
QUESTION:
Create a function named `more_complex_flight(q, w, z)` that takes a list `q`, an integer `w`, and an integer `z` as input and returns a boolean value. The function should return `True` if the list `q` is a palindrome, the sum of its elements does not exceed `w`, and its length is less than or equal to `z`. Otherwise, it should return `False`.
"""

def more_complex_flight(q, w, z):
    if q != q[::-1]:
        return False  # The list is not a palindrome
    if sum(q) > w:
        return False  # The weight exceeds the limit
    if len(q) > z:
        return False  # The length of the list exceeds the distance limit  
    return True