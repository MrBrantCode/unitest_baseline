"""
QUESTION:
Write a function `find_vowel_frequency` that calculates the frequency of each vowel (a, e, i, o, u) in a given string, considering both uppercase and lowercase letters, and returns the frequency of each vowel. The function should have a time complexity of O(n), where n is the length of the input string. The input string is expected to contain only alphabets and special characters, and the output should be the frequency of each vowel (a, e, i, o, u).
"""

def find_vowel_frequency(string):
    freq = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    string = string.lower()

    for c in string:
        if c in freq:
            freq[c] += 1

    return freq