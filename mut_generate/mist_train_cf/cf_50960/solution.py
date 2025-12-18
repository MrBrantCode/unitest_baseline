"""
QUESTION:
Write a function `convert_array(arr)` that takes an array of strings as input and returns the modified array. The function should convert each string to uppercase and replace all vowels ('a', 'e', 'i', 'o', 'u') with 'z'.
"""

def convert_array(arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(arr)):
        word = arr[i].lower()
        new_word = ''
        for char in word:
            if char in vowels:
                new_word += 'z'
            else:
                new_word += char
        arr[i] = new_word.upper()
    return arr