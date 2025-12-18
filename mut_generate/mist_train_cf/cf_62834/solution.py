"""
QUESTION:
Create a function named `count_and_sort_vowels` that takes a string `s` as input. The function should return a list of vowels in the order of their appearance in the string (with each vowel appearing only once) and a dictionary containing the total count of each vowel type, while treating 'a' and 'A' as distinct characters. The function should consider both lowercase and uppercase vowels.
"""

def count_and_sort_vowels(s):
    vowels = "aeiouAEIOU"
    result = []
    counts = {}

    for letter in s:
        if letter in vowels and letter not in result:
            result.append(letter)
            counts[letter] = s.count(letter)

    return result, counts