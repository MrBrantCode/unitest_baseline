"""
QUESTION:
Write a function called `count_letters` that takes a sentence as input and returns a dictionary where the keys are the letters in the sentence and the values are the corresponding counts of each letter. The function should be case-insensitive, exclude numbers and special characters, and not count spaces. The input sentence will not exceed 1000 characters.
"""

def count_letters(sentence):
    # Initialize an empty dictionary to store letter counts
    letter_counts = {}

    # Convert the sentence to lowercase to make it case-insensitive
    sentence = sentence.lower()

    # Iterate over each character in the sentence
    for char in sentence:
        # Check if the character is a letter (excluding numbers and special characters)
        if char.isalpha():
            # If the letter is already in the dictionary, increment its count by 1
            if char in letter_counts:
                letter_counts[char] += 1
            # If the letter is not in the dictionary, add it with a count of 1
            else:
                letter_counts[char] = 1

    # Return the dictionary of letter counts
    return letter_counts