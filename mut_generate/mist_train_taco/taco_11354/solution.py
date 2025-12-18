"""
QUESTION:
Nickname Generator

Write a function, `nicknameGenerator` that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

If the 3rd letter is a consonant, return the first 3 letters.

If the 3rd letter is a vowel, return the first 4 letters. 

If the string is less than 4 characters, return "Error: Name too short".

**Notes:**

- Vowels are "aeiou", so discount the letter "y".
- Input will always be a string.
- Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
- The input can be modified
"""

def generate_nickname(name: str) -> str:
    if len(name) < 4:
        return "Error: Name too short"
    return name[:3 + (name[2] in 'aeiou')]