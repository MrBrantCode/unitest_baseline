"""
QUESTION:
Create a function called `are_anagrams` that takes two string parameters, `string1` and `string2`. The function should determine if `string1` and `string2` are anagrams of each other, considering the following rules:
- Differentiate between uppercase and lowercase letters.
- Ignore special characters and numbers.
- Do not use Python's built-in sorting functions.
"""

def are_anagrams(string1, string2):
    string1 = [s for s in string1 if s.isalpha()]
    string2 = [s for s in string2 if s.isalpha()]

    if len(string1) != len(string2):
        return False

    frequency_dict = {}

    for character in string1:
        if character in frequency_dict:
            frequency_dict[character] += 1
        else:
            frequency_dict[character] = 1

    for character in string2:
        if character not in frequency_dict:
            return False
        if frequency_dict[character] == 1:
            del frequency_dict[character]
        else:
            frequency_dict[character] -= 1

    return len(frequency_dict) == 0