"""
QUESTION:
Create a function named `count_vowels` that takes a string as input and returns a dictionary containing the count and indices of each vowel found in the string. The function should be case-insensitive, ignore non-alphabet characters and spaces, and handle empty strings or strings with only non-alphabet characters and spaces by returning an empty dictionary. The dictionary should have vowels as keys and lists of indices as values.
"""

def count_vowels(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    result = {}
    
    for index, char in enumerate(string):
        if char.isalpha() and char.lower() in vowels:
            vowel = char.lower()
            vowels[vowel] += 1
            if vowel in result:
                result[vowel].append(index)
            else:
                result[vowel] = [index]
    
    return result