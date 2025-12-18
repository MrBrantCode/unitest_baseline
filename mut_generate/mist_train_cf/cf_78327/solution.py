"""
QUESTION:
Create a function `is_palindrome(word)` that checks if a given word is a palindrome. The function should be memory efficient and should not create any additional data structures. The input is a string of characters, and the output should be a boolean value indicating whether the word is a palindrome or not.
"""

def is_palindrome(word):
    start = 0
    end = len(word) - 1

    while start < end:
        # compare characters from start and end
        if word[start] != word[end]:
            return False

        # move towards the middle
        start += 1
        end -= 1

    return True