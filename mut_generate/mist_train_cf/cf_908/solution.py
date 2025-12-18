"""
QUESTION:
Write a function `find_longest_word(s)` that takes a string `s` as input and returns the longest word that contains at least two vowels, two consonants with vowels appearing before consonants, and at least one uppercase letter and one lowercase letter. The input string `s` will not exceed 1000 characters.
"""

def find_longest_word(s):
    longest_word = ""
    max_length = 0

    words = s.split()

    for word in words:
        # Check if the word meets the criteria
        if len(word) > max_length and len([c for c in word if c.islower()]) > 0 and len([c for c in word if c.isupper()]) > 0:
            vowels = 0
            consonants = 0
            for c in word:
                if c.lower() in "aeiou":
                    vowels += 1
                elif c.isalpha():
                    consonants += 1

            if vowels >= 2 and consonants >= 2:
                longest_word = word
                max_length = len(word)

    return longest_word