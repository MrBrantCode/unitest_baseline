"""
QUESTION:
Create a function called `remove_elements_and_repeats(text)` that takes a string `text` as input and returns a string with all vowels, numerical values, and punctuation marks removed, and with no repeated consonants. The function should treat upper and lower case letters as the same when checking for repeats.
"""

def remove_elements_and_repeats(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    seen = []
    
    for char in text:
        if char.isalpha():  # if the character is a letter
            if (char not in vowels) and (char.lower() not in seen):
                result += char
                seen.append(char.lower())
    return result