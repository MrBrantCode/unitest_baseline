"""
QUESTION:
Create a function called `charStats` that takes a string of text as argument and returns two dictionaries, `dict_upper` and `dict_lower`. The function should count the frequency of each uppercase and lowercase English alphabet in the string, ignoring non-alphabetic characters. The function should be case sensitive and efficient for long input strings.
"""

def charStats(text):
    dict_upper = {}
    dict_lower = {}

    for char in text:
        if char.isalpha():
            if char.isupper():
                dict_upper[char] = dict_upper.get(char, 0) + 1
            else:
                dict_lower[char] = dict_lower.get(char, 0) + 1
    return dict_upper, dict_lower