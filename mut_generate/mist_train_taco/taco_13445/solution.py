"""
QUESTION:
Find the first character that repeats in a String and return that character. 

```python
first_dup('tweet') => 't'
first_dup('like') => None
```

*This is not the same as finding the character that repeats first.*
*In that case, an input of 'tweet' would yield 'e'.*
"""

def find_first_repeating_char(s: str) -> str:
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None