"""
QUESTION:
Write a function named `count_vowels` that takes a string `text` as input and returns a dictionary containing the frequency of each vowel (both lowercase and uppercase) in the string. The function should be case sensitive.
"""

def count_vowels(text):
    # List of vowels
    vowels = "aeiouAEIOU"

    # Dictionary to store vowel frequency
    v_count = {i: 0 for i in vowels}

    # Iterate over the text
    for character in text:
        if character in vowels:
            v_count[character] += 1

    return v_count