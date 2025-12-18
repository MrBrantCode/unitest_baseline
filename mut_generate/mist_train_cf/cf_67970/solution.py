"""
QUESTION:
Create a function named `will_it_fly_advanced` that takes three parameters: `q` (a list of integers), `w` (a non-negative integer), and `r` (a non-empty list of integers). The function should return a tuple containing `q` and a new list where each element is the result of `w` divided by the length of `r`, if and only if `q` is a palindrome and the sum of its elements equals `w` and `w` can be evenly divided by the length of `r`. Otherwise, the function should return `False`.
"""

def will_it_fly_advanced(q, w, r):
    """
    Returns a tuple containing q and a new list where each element is the result of w divided by the length of r, 
    if and only if q is a palindrome and the sum of its elements equals w and w can be evenly divided by the length of r.
    
    Args:
    q (list): A list of integers.
    w (int): A non-negative integer.
    r (list): A non-empty list of integers.
    
    Returns:
    tuple or bool: A tuple containing q and a new list if conditions are met, False otherwise.
    """
    if q == q[::-1] and sum(q) == w and w % len(r) == 0:
        avg = w // len(r)
        return (q, [avg for _ in r])
    else:
        return False