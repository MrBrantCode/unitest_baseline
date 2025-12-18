"""
QUESTION:
Create two functions: `is_palindrome` and `make_palindrome`. 

Function `is_palindrome` should determine if a given string is a palindrome, ignoring case, non-alphanumeric characters, and spaces between words, using recursion. The function should return a boolean indicating whether the string is a palindrome.

Function `make_palindrome` should construct the shortest palindrome beginning with the given string, disregarding case and non-alphanumeric characters, and considering spaces between words, within O(n) time complexity. The function should return the resulting palindrome string.
"""

def is_palindrome(string: str) -> bool:
    """ A recursive function checking if a given string is a palindrome by considering spaces among words and disregarding case and non-alphanumeric characters """
    cleaned_input = ''.join(ch for ch in string if ch.isalnum()).lower()
    if len(cleaned_input) <= 1:
        return True
    if cleaned_input[0] != cleaned_input[-1]:
        return False
    return is_palindrome(cleaned_input[1:-1])

def make_palindrome(string: str) -> str:
    """ Build the shortest palindrome beginning with the given string within O(n) time complexity, considering spaces between words, and ignoring case and non-alphanumeric characters.
    - Discern the longest postfix of the supplied string which forms a palindrome.
    - Join to the string's end, the reverse of the string prefix identified before the palindromic suffix.
    """
    cleaned_input = ''.join(ch for ch in string if ch.isalnum()).lower()
    for i in range(len(cleaned_input)):
        if is_palindrome(cleaned_input[i:]):
            return cleaned_input + cleaned_input[:i][::-1]
    return ''