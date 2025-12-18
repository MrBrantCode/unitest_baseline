"""
QUESTION:
Reverse the order of elements in a given array of strings. Ensure that all strings starting with a vowel are placed at the beginning of the reversed array, followed by the strings starting with a consonant, while maintaining the original order within each group. 

The function should be named `reverse_array` and take one argument `arr`, which is the input array of strings. The function should return the modified array of strings.
"""

def entance(arr):
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