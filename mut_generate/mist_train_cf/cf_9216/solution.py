"""
QUESTION:
Create a function called `convert_string` that takes an integer `n` as input and returns an array of size `n` filled with the string "hello", where all vowels in the string are converted to uppercase and all consonants are converted to lowercase.
"""

def convert_string(n):
    arr = ["hello"] * n
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(n):
        converted_str = ''
        for char in arr[i]:
            if char.lower() in vowels:
                converted_str += char.upper()
            else:
                converted_str += char.lower()
        arr[i] = converted_str

    return arr