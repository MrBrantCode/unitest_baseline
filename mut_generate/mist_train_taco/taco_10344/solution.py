"""
QUESTION:
*Debug*   function `getSumOfDigits` that takes positive integer to calculate sum of it's digits. Assume that argument is an integer.

### Example
```
123  => 6
223  => 7
1337 => 15
```
"""

def get_sum_of_digits(num: int) -> int:
    """
    Calculate the sum of the digits of a given positive integer.

    Parameters:
    num (int): A positive integer whose digits are to be summed.

    Returns:
    int: The sum of the digits of the input integer.
    """
    return sum(map(int, str(num)))