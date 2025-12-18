"""
QUESTION:
Create a function named `count_vowels_consonants` that takes a string as input and returns a dictionary containing the count of each vowel (a, e, i, o, u) and the count of each consonant in the string.

The function must ignore case sensitivity, non-alphabetic characters in the string, and return an empty dictionary if the input string does not contain any vowels or consonants. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def count_vowels_consonants(string):
    # Create an empty dictionary to store the counts
    counts = {}

    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()

    # Iterate through each character in the string
    for char in string:
        # Check if the character is alphabetic
        if char.isalpha():
            # Check if the character is a vowel
            if char in 'aeiou':
                # Increment the count of the vowel in the dictionary
                counts[char] = counts.get(char, 0) + 1
            else:
                # Increment the count of the consonant in the dictionary
                counts[char] = counts.get(char, 0) + 1

    # Return the dictionary of counts
    return counts