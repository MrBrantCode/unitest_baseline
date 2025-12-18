"""
QUESTION:
In this exercise, you will have to create a function named tiyFizzBuzz. This function will take on a string parameter and will return that string with some characters replaced, depending on the value:

- If a letter is a upper case consonants, replace that character with "Iron".
- If a letter is a lower case consonants or a non-alpha character, do nothing to that character
- If a letter is a upper case vowel, replace that character with "Iron Yard".
- If a letter is a lower case vowel, replace that character with "Yard".

Ready?
"""

def tiy_fizz_buzz(s: str) -> str:
    def replace_char(c: str) -> str:
        if c.isupper():
            if c in 'AEIOU':
                return 'Iron Yard'
            elif c.isalpha():
                return 'Iron'
        elif c.islower() and c in 'aeiou':
            return 'Yard'
        return c
    
    return ''.join(replace_char(c) for c in s)