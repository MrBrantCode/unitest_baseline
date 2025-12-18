"""
QUESTION:
Given a list of strings, write a function named `reverse_array` that takes this list as input and returns a new list where the order of elements is reversed. However, strings that start with a vowel ('a', 'e', 'i', 'o', 'u') must be placed at the beginning of the reversed list, followed by strings that start with a consonant. The original order of elements within each group should be maintained. The input list contains no duplicate strings.
"""

def reverse_array(arr):
    vowels = []
    consonants = []

    for string in arr:
        if string[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(string)
        else:
            consonants.append(string)

    vowels.reverse()
    consonants.reverse()

    return vowels + consonants