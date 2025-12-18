"""
QUESTION:
Implement the function `find_positions(s1, s2)` that takes two strings `s1` and `s2` as input and returns a list of integers representing the positions of characters in `s1` that can be found in `s2`. 

The function should first remove all consecutive duplicates from both `s1` and `s2`. Then, for each character in the modified `s1`, it should find its position in the modified `s2`. If a character in `s1` does not exist in `s2`, its position should be considered as 0. The position index should start from 0 and the check should be case sensitive. Spaces are also considered as characters.
"""

def find_positions(s1, s2):
    """
    This function takes two strings s1 and s2 as input, removes consecutive duplicates from both,
    and returns a list of integers representing the positions of characters in s1 that can be found in s2.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        list: A list of integers representing the positions of characters in s1 that can be found in s2.
    """

    def remove_consecutive_duplicates(s):
        """Removes consecutive duplicates from a string."""
        res = []
        for i in range(len(s)):
            if i == 0 or s[i] != s[i-1]:
                res.append(s[i])
        return ''.join(res)

    s1_no_dups = remove_consecutive_duplicates(s1)
    s2_no_dups = remove_consecutive_duplicates(s2)

    positions = [s2_no_dups.index(c) if c in s2_no_dups else 0 for c in s1_no_dups]
    return positions