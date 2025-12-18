"""
QUESTION:
Write a function `second_longest_palindrome` that takes an input string and returns the second longest palindrome substring. If no second longest palindrome exists, return "No Second longest palindrome found". The input string may contain duplicate characters.
"""

def second_longest_palindrome(input_string):
    # Generate all possible substrings of the input string
    substrings = [input_string[i: j] for i in range(len(input_string)) for j in range(i + 1, len(input_string) + 1)]

    # Generate a sorted list of all palindromic substrings in the input string, ordered by length in descending order
    palindromes = sorted([p for p in substrings if p == p[::-1]], key=len, reverse=True)

    # Check for the second longest palindrome
    for p in palindromes:
        if len(p) < len(palindromes[0]):
            return p
    return "No Second longest palindrome found"