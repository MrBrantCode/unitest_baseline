"""
QUESTION:
Mr. Square is going on a holiday. He wants to bring 2 of his favorite squares with him, so he put them in his rectangle suitcase.

Write a function that, given the size of the squares and the suitcase, return whether the squares can fit inside the suitcase.
```Python
fit_in(a,b,m,n)
a,b are the sizes of the 2 squares
m,n are the sizes of the suitcase
```

# Example
```Python
fit_in(1,2,3,2) should return True
fit_in(1,2,2,1) should return False
fit_in(3,2,3,2) should return False
fit_in(1,2,1,2) should return False
```
"""

def can_squares_fit_in_suitcase(a, b, m, n):
    """
    Determines if two squares of given sizes can fit inside a suitcase of given dimensions.

    Parameters:
    a (int): Size of the first square.
    b (int): Size of the second square.
    m (int): Width of the suitcase.
    n (int): Height of the suitcase.

    Returns:
    bool: True if the squares can fit inside the suitcase, False otherwise.
    """
    return max(a, b) <= min(m, n) and a + b <= max(m, n)