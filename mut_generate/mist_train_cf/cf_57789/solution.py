"""
QUESTION:
Implement a function `characterCountAndFrequency(submittedString)` that takes a string as input and returns a dictionary with two keys: "total" mapping to the total number of characters in the string, and "frequency" mapping to a dictionary where each key is a unique character in the string and its corresponding value is the character's frequency.
"""

def characterCountAndFrequency(submittedString):
    frequency_dict = {}
    total_chars = 0

    for char in submittedString:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
        total_chars += 1

    return {"total": total_chars, "frequency": frequency_dict}