"""
QUESTION:
Write a function `reverse_words` that takes a string as input, reverses the order of the words, and then reverses the characters within each word. The input string may contain alphabetic characters, spaces, punctuation marks, and special characters. The output should maintain the same capitalization as the input.
"""

def reverse_words(string):
    # Step 1: Split the input string into individual words
    words = string.split()

    # Step 2: Reverse the order of the words
    words = words[::-1]

    # Step 3: Reverse the characters within each word
    words = [word[::-1] for word in words]

    # Step 4: Join the modified list of words back into a string
    reversed_string = ' '.join(words)

    return reversed_string