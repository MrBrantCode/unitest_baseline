"""
QUESTION:
Create a function called `transform_string` that takes a string `s` as input and performs the following operations:
- Replaces all alphabetical characters with their corresponding alphabetical position (A=1, Z=26)
- Converts odd numbers to even
- Triples all special characters
- Creates a dictionary to count the occurrence of each modified character

The function should return the transformed string and the dictionary.

Restrictions:
- The function should return a string of the transformed characters followed by the dictionary of character counts, in the format: 'transformed_string: {character_counts}'
- The function should handle both lowercase and uppercase letters, odd numbers, and special characters
- The function should not modify the original input string
"""

def transform_string(s: str) -> [str, dict]:
    translation = {c: str(i+1) for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}
    translation.update({c.upper(): str(i+1) for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')})
    for i in range(0, 10, 2):
        translation[str(i+1)] = str(i+2)
    special_chars = set(s) - set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') - set('0123456789')
    for c in special_chars:
        translation[c] = c*3
    transformed_s = ''.join(translation.get(c, c) for c in s)
    counter = {}
    for c in transformed_s:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return f"{transformed_s}: {counter}"