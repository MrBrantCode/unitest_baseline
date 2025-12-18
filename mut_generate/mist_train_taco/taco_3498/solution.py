"""
QUESTION:
Write a function that will check whether the permutation of an input string is a palindrome. Bonus points for a solution that is efficient and/or that uses _only_ built-in language functions. Deem yourself **brilliant** if you can come up with a version that does not use _any_ function whatsoever.

# Example 

  `madam` -> True   
  `adamm` -> True   
  `junk`  -> False  
  
## Hint 
The brute force approach would be to generate _all_ the permutations of the string and check each one of them whether it is a palindrome. However, an optimized approach will not require this at all.
"""

def is_permutation_palindrome(input_string: str) -> bool:
    """
    Check whether any permutation of the input string is a palindrome.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if any permutation of the input string is a palindrome, False otherwise.
    """
    return sum((input_string.count(c) % 2 for c in set(input_string))) < 2