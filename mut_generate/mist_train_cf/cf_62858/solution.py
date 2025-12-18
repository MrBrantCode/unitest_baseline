"""
QUESTION:
Write a function `atMostNGivenDigitSet` that calculates the total count of positive integers that can be constructed which are less than or equal to a specified integer `n` using an array of digits. The array `digits` is arranged in a non-decreasing sequence and each `digits[i]` can be used repeatedly to form numbers. All values in `digits` are unique and `digits` is sorted in non-decreasing order.

The function should take two parameters: `digits` and `n`. The `digits` parameter is a list of strings, where each string is a digit from '1' to '9'. The `n` parameter is an integer.

Constraints:
- `1 <= digits.length <= 9`
- `digits[i].length == 1`
- `digits[i]` is a digit from '1' to '9'.
- All the values in `digits` are unique.
- `digits` is sorted in non-decreasing order.
- `1 <= n <= 10^9`
"""

def atMostNGivenDigitSet(digits, n):
    """
    Calculate the total count of positive integers that can be constructed 
    which are less than or equal to a specified integer `n` using an array of digits.

    Args:
    digits (list): A list of strings, where each string is a digit from '1' to '9'.
    n (int): The specified integer.

    Returns:
    int: The total count of positive integers that can be constructed.
    """
    digits = set(int(d) for d in digits)
    n = [int(d) for d in str(n)]
    m, res = len(digits), 0
    
    # Calculate the count of numbers that can be formed by using less than len(n) digits
    for i in range(1, len(n)):
        res += m ** i
        
    # Calculate the count of numbers that can be formed by using len(n) digits
    for i, x in enumerate(n):
        # Calculate the count of numbers that can be formed by using the first i digits
        # and a smaller digit in the ith position
        res += sum(d < x for d in digits) * (m ** (len(n) - i - 1))
        # If the ith digit of n is in the digits set, 
        # we can form a number that is equal to the first i digits of n
        if x not in digits:
            break
    else:
        # If we have checked all the digits and haven't broken the loop, 
        # it means that n can be formed by using the digits
        res += 1
        
    return res