"""
QUESTION:
Write a function `cycpattern_check(a, b)` that checks if the second string or any of its cyclic permutations are found as a continuous subsequence within the first string. The function should ignore case and special characters, accommodate various language-specific characters, and ensure optimal performance for longer string lengths.
"""

import re

def cycpattern_check(a, b):
    """Checks if the second string or any of its cyclic permutations are found as a continuous subsequence within the first string.
    
    The function ignores case and special characters, accommodates various language-specific characters, and ensures optimal performance for longer string lengths.
    """
    
    # Clean the strings: convert to lower case and remove special characters
    a_clean = re.sub(r'\W+', '', a).lower()
    b_clean = re.sub(r'\W+', '', b).lower()
    
    # Create all cyclic permutations of the second string
    cyclic_permutations = [b_clean[i:] + b_clean[:i] for i in range(len(b_clean))]
    
    # Check if any of the permutations is in the first string
    return any(permutation in a_clean for permutation in cyclic_permutations)