"""
QUESTION:
Create a function `count_vowels_and_consonants` that takes a string as input and returns the count of vowels in descending order and the total count of consonants. The function should consider only English alphabet vowels (a, e, i, o, u) and should be case-insensitive, ignoring special characters and numbers. The input string is limited to 100 characters and multiple spaces are treated as a single space. If there are no vowels in the string, the function should indicate this.
"""

def count_vowels_and_consonants(string):
    """
    This function takes a string as input, counts the vowels in descending order 
    and the total count of consonants. The function considers only English alphabet 
    vowels (a, e, i, o, u) and is case-insensitive, ignoring special characters and numbers.

    Parameters:
    string (str): The input string.

    Returns:
    A dictionary with vowels and their counts in descending order, and the total count of consonants.
    """

    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    consonant_count = 0
    string = string.lower()

    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count[char] += 1
            else:
                consonant_count += 1

    vowel_count_descending = sorted(vowel_count.items(), key=lambda x: x[1], reverse=True)

    if all(count == 0 for count in vowel_count.values()):
        return "No vowels found in the string.", consonant_count
    else:
        return dict(vowel_count_descending), consonant_count