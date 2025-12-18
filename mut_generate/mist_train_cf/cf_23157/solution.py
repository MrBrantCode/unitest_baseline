"""
QUESTION:
Create a function named `reverse_array` that takes an array of strings as input. The function should reverse the order of the elements inside the array, but with the condition that all strings starting with a vowel are placed at the beginning of the reversed array, followed by the strings starting with a consonant. The original order of the elements within each group should be maintained. The function should return the modified array.
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