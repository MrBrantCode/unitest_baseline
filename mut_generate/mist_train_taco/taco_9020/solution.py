"""
QUESTION:
Given a string as input, move all of its vowels to the end of the string, in the same order as they were before.

Vowels are (in this kata): `a, e, i, o, u`

Note: all provided input strings are lowercase.

## Examples
```python
"day"    ==>  "dya"
"apple"  ==>  "pplae"
```
"""

def move_vowels(s: str) -> str:
    vowels = 'aeiou'
    consonants = [char for char in s if char not in vowels]
    vowel_chars = [char for char in s if char in vowels]
    return ''.join(consonants + vowel_chars)