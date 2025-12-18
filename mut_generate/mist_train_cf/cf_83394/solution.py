"""
QUESTION:
Write a function `min_insertions` that takes a string `input_string` and two indices `l` and `h` as parameters, and returns the minimum number of characters that need to be inserted to make the substring of `input_string` from index `l` to `h` a palindrome. The function should use recursion.

Write another function `make_palindrome` that takes a string `input_string` as a parameter. If `input_string` is already a palindrome, return it as is. Otherwise, use the `min_insertions` function to determine the minimum number of characters that need to be inserted to make it a palindrome, and insert those characters at the beginning of the string to make it a palindrome.
"""

def min_insertions(s, l, h):
    """
    This function calculates the minimum number of characters that need to be inserted 
    to make the substring of `s` from index `l` to `h` a palindrome.

    Args:
    s (str): The input string.
    l (int): The starting index of the substring.
    h (int): The ending index of the substring.

    Returns:
    int: The minimum number of characters that need to be inserted.
    """
    if l > h:
        return float('inf')
    if l == h: 
        return 0
    if l == h - 1:
        if s[l] == s[h]: 
            return 0
        else:
            return 1 
  
    # Check if the first and last elements of the string are the same. 
    # If not, recursive call, taking the minimum number of elements according to  
    # whether we delete the first or last element
    if s[l] == s[h]: 
        return min_insertions(s, l + 1, h - 1) 
    else:
        return (min(min_insertions(s, l, h - 1), 
               min_insertions(s, l + 1, h)) + 1)

def make_palindrome(s):
    """
    This function takes a string `s` and returns a palindrome string by inserting 
    the minimum number of characters at the beginning of the string.

    Args:
    s (str): The input string.

    Returns:
    str: The resulting palindrome string.
    """
    is_palindrome = s == s[::-1]
    if is_palindrome:
        return s
    else:
        n = len(s)
        min_inserts = min_insertions(s, 0, n - 1)
        for i in range(min_inserts):
            s = s[:i] + s[-(i+1)] + s[i:]
        return s