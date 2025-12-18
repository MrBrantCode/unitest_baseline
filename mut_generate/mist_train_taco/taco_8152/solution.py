"""
QUESTION:
Create a function that takes a string as a parameter and does the following, in this order:

1. replaces every letter with the letter following it in the alphabet (see note below)
2. makes any vowels capital
3. makes any consonants lower case

**Note:** the alphabet should wrap around, so `Z` becomes `A`

So, for example the string `"Cat30"` would return `"dbU30"` (`Cat30 --> Dbu30 --> dbU30`)
"""

def transform_string(s: str) -> str:
    # Step 1: Replace every letter with the letter following it in the alphabet
    def next_letter(c):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
        else:
            return c

    transformed = ''.join(next_letter(c) for c in s)

    # Step 2: Make any vowels capital and consonants lower case
    def transform_case(c):
        if c in 'aeiou':
            return c.upper()
        elif c.isalpha():
            return c.lower()
        else:
            return c

    return ''.join(transform_case(c) for c in transformed)