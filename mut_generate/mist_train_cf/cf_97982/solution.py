"""
QUESTION:
Create a function named `find_longest_palindrome` that takes a list of words and a string as input. The function should return the longest word in the list that can be formed by deleting exactly two characters from the string and is also a palindrome.
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