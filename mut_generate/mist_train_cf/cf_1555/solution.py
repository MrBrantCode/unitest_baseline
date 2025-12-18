"""
QUESTION:
Find all permutations of a given string where the first and last characters are fixed, and the remaining characters are permuted in the middle without repetition. 

Function name: find_permutations 
Restrictions: The first character is fixed, the last character is fixed, no character repetition is allowed, and only the middle characters are permuted.
"""

def find_permutations(s, start, end):
    """
    Find all permutations of a given string where the first and last characters are fixed,
    and the remaining characters are permuted in the middle without repetition.

    Args:
        s (str): The input string.
        start (str): The fixed starting character.
        end (str): The fixed ending character.

    Returns:
        list: A list of all permutations that meet the given conditions.
    """
    # Initialize an empty list to store the permutations
    perms = []

    # Check if the length of the string is less than 3
    if len(s) < 3:
        return perms

    # Check if the start and end characters are the same as the first and last characters of the string
    if s[0] == start and s[-1] == end:
        # Generate all permutations of the middle characters
        from itertools import permutations
        middle_chars = s[1:-1]
        for perm in permutations(middle_chars):
            # Add the start character, the permuted middle characters, and the end character to the list of permutations
            perms.append(start + ''.join(perm) + end)

    # Return the list of permutations
    return perms