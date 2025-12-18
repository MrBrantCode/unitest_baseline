"""
QUESTION:
Create a function named `join_reverse_vowel_strings` that takes an array of strings as input. The function should return a string containing all the strings from the input array that start with a vowel and have at least 3 characters in length, in reverse order, separated by commas, along with the total number of vowels in the resulting string.
"""

def join_reverse_vowel_strings(arr):
    result = []
    vowel_count = 0
    for word in arr:
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u'] and len(word) >= 3:
            result.append(word)
            vowel_count += sum(1 for letter in word if letter.lower() in ['a', 'e', 'i', 'o', 'u'])
    result.reverse()
    return ','.join(result), vowel_count