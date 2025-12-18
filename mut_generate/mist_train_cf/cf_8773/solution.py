"""
QUESTION:
Create a function `reverse_array` that takes an array of strings as input and returns the array with the order of the elements reversed. The strings starting with a vowel ('a', 'e', 'i', 'o', or 'u') should be placed at the beginning of the reversed array, followed by the strings starting with a consonant. The original order of the elements within each group should be maintained.
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