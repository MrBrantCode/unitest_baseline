"""
QUESTION:
Write a function `consonants_count` that takes a string as input and returns the number of consonants present in the string. Consonants refer to all alphabets except 'a', 'e', 'i', 'o', and 'u', and are case-insensitive. The function should overlook non-alphabet characters and unique symbols in the word.
"""

def consonants_count(s):
    vowels = "aeiou"
    consonants = 0

    # Convert the string to lowercase
    s = s.lower()

    # Check each character in the string
    for char in s:
        # Increase the count if it's an alphabet character not in the vowels list
        if char.isalpha() and char not in vowels:
            consonants += 1
    return consonants