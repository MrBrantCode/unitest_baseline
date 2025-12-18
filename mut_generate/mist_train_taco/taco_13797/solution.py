"""
QUESTION:
The alphabetized kata
---------------------

Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply be removed!

The input is restricted to contain no numerals and only words containing the english alphabet letters.

Example: 

```python
alphabetized("The Holy Bible") # "BbeehHilloTy"
```

_Inspired by [Tauba Auerbach](http://www.taubaauerbach.com/view.php?id=73)_
"""

def alphabetized(s: str) -> str:
    """
    Re-orders the characters of the input string into a new string in case-insensitively-alphabetical-order-of-appearance.
    Whitespace and punctuation are removed.

    Parameters:
    s (str): The input string containing only English alphabet letters, whitespace, and punctuation.

    Returns:
    str: A new string with characters sorted in case-insensitively-alphabetical-order-of-appearance.
    """
    return ''.join(sorted(filter(str.isalpha, s), key=str.lower))