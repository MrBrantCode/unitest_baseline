"""
QUESTION:
Implement a function called `organize_array` that takes a list of strings as input and returns a new list with the following conditions: 
- all strings starting with a vowel (a, e, i, o, u) should be placed at the beginning of the array, 
- the strings starting with a vowel should be in alphabetical order, 
- the remaining strings should be in alphabetical order, 
- the final array should not contain any duplicate strings.
"""

from typing import List

def organize_array(strings: List[str]) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_strings = [string for string in strings if string[0].lower() in vowels]
    remaining_strings = [string for string in strings if string[0].lower() not in vowels]
    result = sorted(list(set(vowel_strings))) + sorted(list(set(remaining_strings)))
    
    return result