"""
QUESTION:
Construct the lexicographically smallest palindrome by inserting exactly one character into the given string of lowercase English letters. If the string is already a palindrome, return it as is. If no such palindrome can be formed, return an empty string. The function name should be `construct_min_palindrome` and it should take one argument `non_palindrome`. The length of `non_palindrome` will be between 1 and 1000 inclusive.
"""

def construct_min_palindrome(non_palindrome):
    # if the string is already a palindrome, return the string itself
    if non_palindrome == non_palindrome[::-1]:
        return non_palindrome
    
    # if not, append the smallest character from the string to its end to make a palindrome
    else:
        return non_palindrome + min(non_palindrome)