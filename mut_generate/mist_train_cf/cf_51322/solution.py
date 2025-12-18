"""
QUESTION:
Create a function named `check_palindrome` that takes a string `input_str` as input. The function should return `True` if the input string is a palindrome, contains all English vowels ('a', 'e', 'i', 'o', 'u'), and does not have consecutive repeated vowels. The function should ignore punctuation, whitespace, and is case-insensitive.
"""

def check_palindrome(input_str):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    input_str = input_str.replace(' ', '').replace(',','').replace('.','').replace('!','').replace('?','').lower()
    if set(input_str) & vowels != vowels:
        return False

    i, j = 0, len(input_str) - 1
    last_vowel = ''
    while i <= j:
        if not input_str[i].isalpha():
            i += 1
            continue
        if not input_str[j].isalpha():
            j -= 1
            continue
        if input_str[i] in vowels:
            if last_vowel == input_str[i]:
                return False
            last_vowel = input_str[i]

        if input_str[i] != input_str[j]:
            return False
        i += 1
        j -= 1
    return True