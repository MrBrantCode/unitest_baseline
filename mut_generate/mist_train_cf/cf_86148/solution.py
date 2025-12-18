"""
QUESTION:
Implement a function `check_tuple(t)` that takes a tuple of strings as input. The function should return a tuple containing the total number of characters in all palindrome strings and a list of strings that are not palindromes. A palindrome string is a string that reads the same backwards as forwards.
"""

def check_tuple(t):
    """Check the palindromes in the tuple, count their characters and return non-palindrome strings"""
    non_palindromes = []
    char_count = 0

    # iterate over each string in the tuple
    for s in t:
        # if it's a palindrome, count its characters
        if s == s[::-1]:
            char_count += len(s)
        else:
            # if it's not a palindrome, add it to the non_palindromes list
            non_palindromes.append(s)
 
    return char_count, non_palindromes