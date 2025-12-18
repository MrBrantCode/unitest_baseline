"""
QUESTION:
Quite recently it happened to me to join some recruitment interview, where my first task was to write own implementation of built-in split function. It's quite simple, is it not?

However, there were the following conditions:

* the function **cannot** use, in any way, the original `split` or `rsplit` functions,
* the new function **must** be a generator,
* it should behave as the built-in `split`, so it will be tested that way -- think of `split()` and `split('')`


*This Kata will control if the new function is a generator and if it's not using the built-in split method, so you may try to hack it, but let me know if with success, or if something would go wrong!*

Enjoy!
"""

import re

def custom_split_generator(string, delimiter=None):
    """
    A custom generator function that splits a string by a specified delimiter.

    Parameters:
    - string (str): The input string to be split.
    - delimiter (str, optional): The delimiter used to split the string. If not provided, the function will split by whitespace.

    Yields:
    - str: Parts of the string split by the specified delimiter.

    Raises:
    - ValueError: If the delimiter is an empty string.
    """
    if delimiter == '':
        raise ValueError('empty delimiter')
    
    if delimiter is None:
        delimiter = '\\s+'
    else:
        delimiter = re.escape(delimiter)
    
    pos = 0
    for m in re.finditer(delimiter, string):
        yield string[pos:m.start()]
        pos = m.end()
    
    yield string[pos:]