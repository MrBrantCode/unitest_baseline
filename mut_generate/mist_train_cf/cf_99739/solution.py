"""
QUESTION:
Implement a Python function called "vowel_trio" that takes a list of strings as input. The function should return a new list containing only the strings that start with the letter 'y' and have the third vowel 'i' after 'y'. The function should only consider lowercase vowels as valid candidates.
"""

def vowel_trio(strings):
    vowels = ["a", "e", "i", "o", "u"]
    new_strings = []
    for string in strings:
        if string[0].lower() == 'y':
            count = 0
            for letter in string[1:]:
                if letter.lower() in vowels:
                    count += 1
                    if count == 3 and letter.lower() == 'i':
                        new_strings.append(string)
                        break
    return new_strings