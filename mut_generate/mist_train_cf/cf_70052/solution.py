"""
QUESTION:
Write a recursive function `recursive_func(z)` that takes an integer `z` as input, and uses global variables `x` and `y`. The function should recursively assign the value of `z` to `x` directly and `y` indirectly via `x` until `z` equals zero, decreasing `z` by one at each recursive step.
"""

def recursive_func(z):
    global x 
    global y 

    if z < 0: 
        return 
    else:
        x = z 
        y = x 
        recursive_func(z-1) 