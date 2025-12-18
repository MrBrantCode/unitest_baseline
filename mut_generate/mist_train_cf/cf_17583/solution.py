"""
QUESTION:
Write a function `reverse_words` that takes a string as input, reverses the order of words, reverses the characters within each word, and returns the resulting string. The function should maintain the same capitalization as the input string and handle strings containing alphabetic characters, spaces, punctuation marks, and special characters.
"""

def reverse_words(s):
    # Step 1: Split the input string into individual words
    words = s.split()

    # Step 2: Reverse the order of the words
    words = words[::-1]

    # Step 3: Reverse the characters within each word
    words = [word[::-1] for word in words]

    # Step 4: Join the modified list of words back into a string
    return ' '.join(words)