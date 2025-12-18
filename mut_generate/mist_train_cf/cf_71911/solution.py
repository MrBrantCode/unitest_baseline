"""
QUESTION:
Write a function `beneficial_divisions(s)` that takes a string `s` as input and returns the quantity of beneficial divisions that can be performed on `s`. A division is deemed beneficial if `s` can be divided into two non-empty substrings `p` and `q` such that their concatenation equals `s` and the quantity of unique characters in `p` and `q` are identical, with no overlapping characters between `p` and `q`. The input string `s` only contains lowercase English alphabets and has a length between 1 and 10^5.
"""

def beneficial_divisions(s):
    """
    Calculate the quantity of beneficial divisions that can be performed on string s.
    
    A division is deemed beneficial if s can be divided into two non-empty substrings 
    p and q such that their concatenation equals s and the quantity of unique characters 
    in p and q are identical, with no overlapping characters between p and q.

    Args:
    s (str): The input string containing lowercase English alphabets.

    Returns:
    int: The quantity of beneficial divisions.
    """
    left, right = {}, {}
    for char in s:
        if char in right:
            right[char] += 1
        else:
            right[char] = 1

    count = 0
    for char in s:
        if char in left:
            left[char] += 1
        else:
            left[char] = 1
        right[char] -= 1
        if right[char] == 0:
            del right[char]
        if len(left) == len(right):
            count += 1

    return count