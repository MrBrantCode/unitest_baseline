"""
QUESTION:
Write a function `is_anagram_of_reversed(word)` that determines if a given word is an anagram of its reverse. The function should be case-insensitive and return a boolean value indicating whether the word is an anagram of its reverse. The input is a string, and the function should handle all possible string inputs.
"""

def is_anagram_of_reversed(word):
    # Convert the word to lower case to ignore the case of the letters
    word = word.lower()

    # Reverse the word
    reverse_word = word[::-1]

    # Check if the sorted form of the word and its reverse are the same
    if sorted(reverse_word) == sorted(word):
        return True
    else:
        return False