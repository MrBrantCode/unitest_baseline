"""
QUESTION:
Write a function called `count_vowels` that takes a string as input and returns a dictionary where the keys are the unique vowels 'a', 'e', 'i', 'o', 'u' and the values are tuples containing the count and index of the first occurrence of the vowel in the string. The function should ignore case, have a time complexity of O(n), and return an empty dictionary if the string does not contain any of the specified vowels. The index is 0-based.
"""

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_dict = {}
    index_dict = {}

    for vowel in vowels:
        count_dict[vowel] = 0
        index_dict[vowel] = None

    for i, char in enumerate(string):
        lowercase_char = char.lower()
        if lowercase_char in vowels:
            count_dict[lowercase_char] += 1
            if index_dict[lowercase_char] is None:
                index_dict[lowercase_char] = i

    result_dict = {}
    for vowel in vowels:
        if count_dict[vowel] > 0:
            result_dict[vowel] = (count_dict[vowel], index_dict[vowel])

    return result_dict