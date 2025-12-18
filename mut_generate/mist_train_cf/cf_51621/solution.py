"""
QUESTION:
Write a function `advanced_custom_sort` that takes a list `l`, two integers `n` and `m`, a sort directive `s` ('asc' or 'desc'), an arithmetic function `f` ('square' or 'cube'), and a rotation value `r`. The function returns a new list where elements outside the range `(n, m)` remain the same, elements within the range `(n, m)` are transformed by function `f` and sorted according to `s`, and the resulting list is rotated `r` times. 

Function `f` can transform an element `x` in two ways: 'square' (x is changed to x squared) or 'cube' (x is changed to x cubed).
"""

def advanced_custom_sort(l: list, n: int, m: int, s: str, r: int, f: str) -> list:
    """
    This function takes a list l, two integers n and m, a sort directive s ('asc' or 'desc'), 
    an arithmetic function f ('square' or 'cube') and a rotation value r, 
    returning a new list. 
    In the new list, elements whose indices do not fall within the range of (n, m) remain the same as in l, 
    while the elements values within the range (n, m) are transformed by the function 'f' 
    of their corresponding indices in l, sorted according to s. 
    The list is then rotated r times.

    Function f can transform an element x in the following ways:
    'square' - x is changed to x squared.
    'cube' - x is changed to x cubed.

    Parameters:
    l (list): Input list
    n (int): Start index of the range
    m (int): End index of the range
    s (str): Sort directive ('asc' or 'desc')
    r (int): Rotation value
    f (str): Arithmetic function ('square' or 'cube')

    Returns:
    list: The transformed, sorted and rotated list
    """
    
    transform = {'square': lambda x: x*x,
                 'cube': lambda x: x*x*x}

    transformed = [transform[f](x) if n<=i<m else x for i,x in enumerate(l)]
    sorted_l = transformed[:n] + sorted(transformed[n:m], reverse= s == 'desc') + transformed[m:]
    return sorted_l[-r:] + sorted_l[:-r]