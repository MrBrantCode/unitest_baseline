"""
QUESTION:
The [Ones' Complement](https://en.wikipedia.org/wiki/Ones%27_complement) of a binary number is the number obtained by swapping all the 0s for 1s and all the 1s for 0s. For example:

```
onesComplement(1001) = 0110
onesComplement(1001) = 0110
```

For any given binary number,formatted as a string, return the Ones' Complement of that number.
"""

def ones_complement(binary_str: str) -> str:
    """
    Returns the Ones' Complement of a given binary number.

    Parameters:
    binary_str (str): The input binary number as a string.

    Returns:
    str: The Ones' Complement of the input binary number as a string.
    """
    return binary_str.translate(str.maketrans('01', '10'))