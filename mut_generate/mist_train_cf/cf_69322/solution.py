"""
QUESTION:
Construct a function named `count_vowels` that calculates the cumulative count of vowels from a given list of words, subject to the following conditions:

- The word must start with a vowel.
- The word must not end with a vowel.
- The word must be at least 3 characters long.
- The word must not be a palindrome.
- The word must only contain alphabetic characters.
- The word must not contain any repeated letters.

The function should iterate through the list of words, filter out the words that do not meet these conditions, and return the total count of vowels from the remaining words.
"""

def count_vowels(words):
    total_vowels = 0
    vowels = set('aeiou')
    
    for word in words:
        word = word.lower()
        if word[0] in vowels and word[-1] not in vowels and len(word) >= 3 and word != word[::-1]:
            if word.isalpha() and len(set(word)) == len(word):  # Checking for alphabets and no repeated letters
                for letter in word:
                    if letter in vowels:
                        total_vowels += 1
    return total_vowels