"""
QUESTION:
Write a function named `count_consonants` that takes a string `text` as input and returns the number of consonants present in the string, excluding non-alphanumeric characters and considering both lowercase and uppercase letters. The input string may contain alphanumeric characters, spaces, and punctuation.
"""

def count_consonants(text):
    # string of vowels
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    # Remove spaces and punctuation, then convert to lowercase
    text = ''.join(e for e in text if e.isalnum()).lower()

    # count the consonants
    count = 0
    for letter in text:
        if letter not in vowels and letter.isalpha():
            count += 1

    return count