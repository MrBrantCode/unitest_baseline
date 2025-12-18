"""
QUESTION:
Write a function `char_frequency(str1)` that takes a string `str1` as input and returns a dictionary containing the frequency of each distinct character in the string. The function should count the occurrence of each unique character in the string and store it in the dictionary. The function should work for any given string and should not consider the case of the characters (i.e., 'a' and 'A' are considered the same).
"""

def char_frequency(str1):
    dict = {}
    for n in str1.lower():
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict