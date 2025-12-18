"""
QUESTION:
Write a function `is_palindrome` that takes a list of strings as input. The function should return a list of tuples, where each tuple contains a boolean indicating whether the corresponding input string is a palindrome (ignoring non-alphabetic characters) and the longest palindrome substring found in each input string (considering only alphabetic characters). If the input string is not a palindrome, the second element of the tuple should be an empty string.
"""

def is_palindrome(strings):
    results = []
    for string in strings:
        cleaned_string = ''.join(char for char in string if char.isalpha()).lower()
        reversed_string = cleaned_string[::-1]
        is_palindrome = cleaned_string == reversed_string
        longest_palindrome = cleaned_string if is_palindrome else ""
        results.append((is_palindrome, longest_palindrome))
    return results