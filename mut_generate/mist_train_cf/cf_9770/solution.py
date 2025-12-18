"""
QUESTION:
Write a function named `reverse_words` that takes a string as input and returns a string with each word's characters reversed while maintaining the original capitalization of each word. The input string can contain words with all uppercase, all lowercase, or mixed capitalization.
"""

def reverse_words(s):
    words = s.split()
    reversed_words = []

    for word in words:
        if word.isupper():
            reversed_words.append(word[::-1].upper())
        elif word.islower():
            reversed_words.append(word[::-1].lower())
        else:
            reversed_word = ""
            for char in word:
                if char.isupper():
                    reversed_word += char.lower()
                else:
                    reversed_word += char.upper()
            reversed_words.append(reversed_word[::-1])

    return " ".join(reversed_words)