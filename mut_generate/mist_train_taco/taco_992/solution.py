"""
QUESTION:
In this kata you will have to change every letter in a given string to the next letter in the alphabet. You will write a function `nextLetter` to do this. The function will take a single parameter `s` (string).

Examples:

```
"Hello" --> "Ifmmp"

"What is your name?" --> "Xibu jt zpvs obnf?"

"zoo" --> "app"

"zzZAaa" --> "aaABbb"
```

Note: spaces and special characters should remain the same. Capital letters should transfer in the same way but remain capitilized.
"""

def next_letter(s: str) -> str:
    def shift_char(c: str) -> str:
        if c.isalpha():
            if c in 'zZ':
                return chr(ord(c) - 25)
            else:
                return chr(ord(c) + 1)
        else:
            return c
    
    return ''.join(shift_char(c) for c in s)