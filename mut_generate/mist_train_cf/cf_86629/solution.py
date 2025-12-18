"""
QUESTION:
Create a function named `get_first_consonants` that takes a string as input and returns a string containing the first consonant of each word in lowercase, ignoring vowels, numbers, and special characters. The function should have a time complexity of O(n), where n is the length of the string.
"""

def get_first_consonants(string):
    result = ""
    words = string.split()

    for word in words:
        consonants = ""
        for char in word:
            if char.lower() not in "aeiou" and not char.isdigit():
                consonants += char.lower()
                break  # Only consider the first consonant of each word

        result += consonants

    return result