"""
QUESTION:
Create a function `remove_vowels` that takes a string of lowercase letters as input and returns a new string with all vowels removed. The remaining letters should be sorted in descending order. The function should have a space complexity of O(1) and a time complexity of O(n log n), where n is the length of the input string.
"""

def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ''.join([char for char in string if char not in vowels])
    return ''.join(sorted(new_string, reverse=True))