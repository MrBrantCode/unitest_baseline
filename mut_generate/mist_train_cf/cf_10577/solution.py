"""
QUESTION:
Write a function `find_common_letters(string1, string2)` that finds the common alphabetic letters between two input strings and returns their frequencies. The function should be case-insensitive and ignore non-alphabetic characters. The result should be a dictionary where the keys are the common letters and the values are their frequencies.
"""

def find_common_letters(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    common_letters = {}
    for letter in string1:
        if letter.isalpha() and letter in string2:
            if letter in common_letters:
                common_letters[letter] += 1
            else:
                common_letters[letter] = 1
    return common_letters