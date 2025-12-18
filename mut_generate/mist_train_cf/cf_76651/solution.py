"""
QUESTION:
Write a function `count_letters` that takes a string `s` as input and returns a dictionary with the total number of occurrences of each lowercase Roman letter in the string, along with the total number of all lowercase letters. The function should be case-insensitive, meaning it should count both lowercase and uppercase Roman letters. Non-alphabetic characters should be ignored.
"""

from collections import Counter

def count_letters(s):
    s = s.lower()  
    count_dict = dict(Counter(s))  
    roman_english_letters = 'abcdefghijklmnopqrstuvwxyz'  
    result = {}
    total_count = 0
    for letter in roman_english_letters:
        if letter in count_dict:
            result[letter] = count_dict[letter]
            total_count += count_dict[letter]
    return result, total_count