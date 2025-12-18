"""
QUESTION:
Write a function `find_longest_palindrome` that takes a list of words and a string as input. The function should find the longest word in the list that can be formed by deleting exactly two characters from the string and is a palindrome. The function should return the longest palindrome word. 

Note that the function should iterate through all possible deletions of two characters from the string and compare them to the words in the list, checking for both a match and palindrome property.
"""

def find_longest_palindrome(words, string):
    longest_palindrome = ''
    for word in words:
        if len(word) < len(longest_palindrome):
            continue
        for i in range(len(string)):
            for j in range(i+1, len(string)):
                if string[:i] + string[i+1:j] + string[j+1:] == word and word == word[::-1]:
                    longest_palindrome = word
    return longest_palindrome