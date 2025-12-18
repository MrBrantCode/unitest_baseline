"""
QUESTION:
Create a function `string_filter` that takes a list of strings as input and returns a new list of strings that meet the following conditions: start with 't', end with a vowel ('a', 'e', 'i', 'o', 'u'), and have a length greater than 5 characters. The time complexity should be no greater than O(n), where n is the number of elements in the input list.
"""

def string_filter(lst):
    vowels = 'aeiou'
    return [s for s in lst if s[0] == 't' and s[-1] in vowels and len(s) > 5]