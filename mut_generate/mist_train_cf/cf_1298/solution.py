"""
QUESTION:
Create a function named `count_vowels_and_consonants` that takes in a string and returns a dictionary containing the count of each vowel (a, e, i, o, u) and the count of each consonant in the string. The function should ignore case sensitivity, ignore any non-alphabetic characters in the string, and return an empty dictionary if the input string does not contain any vowels or consonants. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def count_vowels_and_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = {}

    for char in string.lower():
        if char.isalpha():
            if char in vowels:
                counts[char] = counts.get(char, 0) + 1
            else:
                counts[char] = counts.get(char, 0) + 1

    return counts