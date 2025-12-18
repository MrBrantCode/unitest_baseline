"""
QUESTION:
Write a function named `replace_vowels` that takes two parameters: `string` and `replace_char`. The function should replace all vowels in the `string` with the `replace_char` and return the modified string. The function should have a time complexity of O(n), where n is the length of the input `string`, and a space complexity of O(1), excluding the space needed for the input and output strings.
"""

def replace_vowels(string, replace_char):
    vowels = 'aeiouAEIOU'
    result = ''
    
    for char in string:
        if char in vowels:
            result += replace_char
        else:
            result += char
    
    return result