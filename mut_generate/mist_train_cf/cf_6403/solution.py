"""
QUESTION:
Write a function called `find_longest_non_palindrome_word(text)` that takes a string `text` as input, where the string contains only alphabetical characters, spaces, and uppercase letters. The function should return the longest word in the text that is not a palindrome and contains at least one uppercase letter. If there are multiple words with the same length, return the first occurrence of the longest non-palindromic word.
"""

def find_longest_non_palindrome_word(text):
    # Split the text into words
    words = text.split()

    # Initialize variables to store the longest non-palindrome word and its length
    longest_word = ""
    longest_length = 0

    # Iterate through each word in the text
    for word in words:
        # Check if the word contains at least one uppercase letter
        if any(letter.isupper() for letter in word):
            # Check if the word is not a palindrome
            if word != word[::-1]:
                # Check if the word is longer than the current longest non-palindrome word
                if len(word) > longest_length:
                    longest_word = word
                    longest_length = len(word)

    return longest_word