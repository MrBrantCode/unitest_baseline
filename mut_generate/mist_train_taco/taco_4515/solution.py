"""
QUESTION:
In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs only once. 

```Haskell
Rules are: (1) the letters are adjacent in the English alphabet, and (2) each letter occurs only once.

For example: 
solve("abc") = True, because it contains a,b,c
solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
solve("dabc") = True, because it contains a, b, c, d
solve("abbc") = False, because b does not occur once.
solve("v") = True
```
All inputs will be lowercase letters. 

More examples in test cases. Good luck!
"""

import string

def is_consecutive_alphabet(st: str) -> bool:
    """
    Check if the input string contains consecutive letters as they appear in the English alphabet
    and if each letter occurs only once.

    Parameters:
    st (str): A string containing lowercase letters.

    Returns:
    bool: True if the string contains consecutive letters and each letter occurs only once, False otherwise.
    """
    sorted_st = ''.join(sorted(st))
    return sorted_st in string.ascii_lowercase