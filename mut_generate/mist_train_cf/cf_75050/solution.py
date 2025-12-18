"""
QUESTION:
Write a function `count_alphabets_in_strings` that takes a list of strings as input, transforms each string into a dictionary key, and assigns the corresponding value as the count of alphabetic characters in the string. The function should return a dictionary containing the alphabetic character counts for each input string.
"""

def count_alphabets_in_strings(arr):
    result_dict = {}
    for string in arr:
        count = 0
        for char in string:
            if char.isalpha():
                count += 1
        result_dict[string] = count
    return result_dict