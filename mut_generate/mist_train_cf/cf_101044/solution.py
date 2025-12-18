"""
QUESTION:
Create a function called `say_hello` that takes an integer argument `n` and returns an array of strings containing the message "Hello, world!" repeated `n` times. Use the numpy library to create and manipulate the array.
"""

import numpy as np

def say_hello(n):
    msg = np.array(['Hello, world!'])
    return np.tile(msg, n)