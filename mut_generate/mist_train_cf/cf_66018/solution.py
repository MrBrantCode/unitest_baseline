"""
QUESTION:
Design a function `if_can_fly(q, w, e)` that evaluates whether object `q` can fly under the given gravity `e`. The function should return `True` if the object can fly and `False` otherwise. The object can fly if three conditions are met: the object is represented as a palindrome list, the total weight of its components does not exceed the upper limit weight `w`, and the gravity `e` is present (though its value does not affect the outcome).
"""

def if_can_fly(q, w, e): 
    # Check if the list is a palindrome
    if q != q[::-1]:
        return False
    # Check if the total weight exceeds the limit
    if sum(q) > w:
        return False
    # If both conditions are passed, return true
    return True