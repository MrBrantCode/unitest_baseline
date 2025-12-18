"""
QUESTION:
Create a function `count_vowels` that takes a string as input and returns a dictionary with the count and positions of each vowel in the string. The function should ignore non-alphabet characters and spaces, handle uppercase vowels, and return an empty dictionary if the string is empty or contains only non-alphabet characters and spaces.
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