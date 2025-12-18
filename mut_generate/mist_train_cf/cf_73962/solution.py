"""
QUESTION:
Write a function `will_it_fly` that takes a list of integers `q`, and three integers `w`, `x`, and `y`. The function should return `True` if `q` can "fly", and `False` otherwise. 

For `q` to "fly", it must satisfy four conditions: 
1. `q` must be palindromic (i.e., the list is symmetrical). 
2. The sum of all elements in `q` must be less than or equal to `w`.
3. The sum of every alternate element in `q` must be less than or equal to `x`.
4. The sum of the remaining elements in `q` must be less than or equal to `y`.

Note that the function should be efficient for large lists and handle edge cases properly.
"""

def will_it_fly(q, w, x, y):
    """
    Checks if a list of integers q can "fly" based on four conditions:
    1. q must be palindromic (i.e., the list is symmetrical).
    2. The sum of all elements in q must be less than or equal to w.
    3. The sum of every alternate element in q must be less than or equal to x.
    4. The sum of the remaining elements in q must be less than or equal to y.

    Args:
        q (list): A list of integers.
        w (int): The maximum sum of all elements in q.
        x (int): The maximum sum of every alternate element in q.
        y (int): The maximum sum of the remaining elements in q.

    Returns:
        bool: True if q can "fly", False otherwise.
    """

    # Check if q is palindromic
    if q != q[::-1]:
        return False
    
    # Check if the sum of all elements in q is less than or equal to w
    if sum(q) > w:
        return False
    
    # Check if the sum of every alternate element in q is less than or equal to x
    if sum(q[::2]) > x:
        return False
    
    # Check if the sum of the remaining elements in q is less than or equal to y
    if sum(q[1::2]) > y:
        return False
    
    # If all conditions are met, return True
    return True