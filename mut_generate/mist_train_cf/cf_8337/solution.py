"""
QUESTION:
Write a function `convert_text(text)` that takes a string `text` as input and returns the modified string where all vowels are converted to lowercase and their order is reversed. The time complexity of the solution should be O(n), where n is the length of the input string.
"""

def convert_text(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    converted_text = ''
    vowel_text = ''
    for char in text:
        if char.lower() in vowels:
            vowel_text += char.lower()
        converted_text += char.lower()
    vowel_text = vowel_text[::-1]
    final_text = ''
    vowel_index = 0
    for char in converted_text:
        if char.lower() in vowels:
            final_text += vowel_text[vowel_index]
            vowel_index += 1
        else:
            final_text += char
    return final_text