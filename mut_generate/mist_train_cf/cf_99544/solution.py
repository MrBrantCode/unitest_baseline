"""
QUESTION:
Create a function `find_longest_palindrome(words, string)` that finds the longest palindrome word in the list `words` that can be formed by deleting exactly two characters from the string `string`. The function should return the longest palindrome word that meets these conditions. The input `words` is a list of strings, and `string` is a single string.
"""

def find_longest_palindrome(words, string):
    longest_palindrome = ''
    for word in words:
        if len(word) < len(longest_palindrome):
            continue
        for i in range(len(string)):
            for j in range(i+1, len(string)):
                if string[:i] + string[j:] == word and word == word[::-1]:
                    longest_palindrome = word
    return longest_palindrome