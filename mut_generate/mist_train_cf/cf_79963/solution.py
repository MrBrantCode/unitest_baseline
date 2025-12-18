"""
QUESTION:
Write a function `min_palindrome(word)` that determines the minimum length of a palindrome that can be constructed from the given string `word`. The function should return the minimum length of the palindrome. The input string `word` contains only lowercase letters.
"""

def min_palindrome(word):
    letters = {}
    for char in word:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    odd_count = sum(1 for count in letters.values() if count % 2 != 0)

    if odd_count > 1:
        return len(word) + odd_count - 1
    else:
        return len(word)