"""
QUESTION:
Create two functions in Python: `is_palindrome` and `is_mirrored`. 

Function `is_palindrome(n)` checks if a given number `n` is a palindrome. 

Function `is_mirrored(n, ignore_case=True, ignore_non_numbers=True)` checks if a number `n` is a palindrome or a mirrored palindrome under certain conditions. The function should take two optional parameters: `ignore_case` to perform a case-insensitive check, and `ignore_non_numbers` to ignore non-number characters in `n`. The function should return `True` if `n` is a palindrome or a mirrored palindrome, and `False` otherwise.
"""

def entrance(n, ignore_case=True, ignore_non_numbers=True):
    """Check if a number is a palindrome or a mirrored palindrome under certain conditions.

    Args:
    n: The number to check.
    ignore_case: If true, perform a case-insensitive check. This only really makes sense if n is a string with alphanumeric characters.
    ignore_non_numbers: If true, ignore non-number characters in n.

    Returns:
    True if n is a palindrome or a mirrored palindrome, and False otherwise.
    """
    n = str(n)
    # Convert to lower case if the check is case-insensitive.
    if ignore_case:
        n = n.lower()
   
    # Remove non-number characters if necessary.
    if ignore_non_numbers:
        n = ''.join(c for c in n if c.isdigit())
   
    # Check if the number is a palindrome or mirrored palindrome.
    return n == n[::-1] or n == str(int(n[::-1]))