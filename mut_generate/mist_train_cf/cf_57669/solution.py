"""
QUESTION:
Write a function `longestPalindrome(s)` that takes a string `s` as input and returns the longest symmetrical substring (palindrome) in `s`. The function should be able to handle cases where the palindrome has an odd or even length, and it should return the longest palindrome found in the entire string. The input string `s` only contains alphanumeric characters.
"""

def longestPalindrome(s):
    """
    This function finds the longest symmetrical substring (palindrome) in a given string.
    
    Parameters:
    s (str): The input string containing only alphanumeric characters.
    
    Returns:
    str: The longest palindrome found in the entire string.
    """
    if not s or len(s) < 1:
        return ""

    start = 0
    end = 0
    
    def expand_around_center(left, right):
        """
        This helper function tries to expand a palindrome around the center of the string.
        
        Parameters:
        left (int): The left index of the center.
        right (int): The right index of the center.
        
        Returns:
        int: The length of the palindrome.
        """
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        length = max(len1, len2)
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    
    return s[start:end + 1]