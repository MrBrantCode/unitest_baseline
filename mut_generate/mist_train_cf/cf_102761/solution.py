"""
QUESTION:
Write a function called `fill_array_squares` that initializes an array of size `n` and fills it with squares of numbers from 0 to `n-1`. The function should return the filled array.

Restrictions: The function should use a loop to iterate over the array indices and assign the square of each index to the corresponding array element. The function should also handle the case where `n` is 0 or a negative number, returning an empty array in such cases.

Note: The function should be implemented in Python.
"""

def fill_array_squares(n):
    """
    Initializes an array of size n and fills it with squares of numbers from 0 to n-1.
    
    Args:
    n (int): The size of the array.
    
    Returns:
    list: A list of squares of numbers from 0 to n-1.
    """
    if n <= 0:
        return []
    arr = [0] * n
    for i in range(n):
        arr[i] = i * i
    return arr