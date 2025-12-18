"""
QUESTION:
### Description:

 Replace all vowel to exclamation mark in the sentence. `aeiouAEIOU` is vowel.

### Examples

```
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
```
"""

def replace_vowels_with_exclamation(sentence: str) -> str:
    return ''.join(('!' if c in 'aeiouAEIOU' else c for c in sentence))