"""
QUESTION:
Take 2 strings `s1` and `s2` including only letters from `a`to `z`.
Return a new **sorted** string, the longest possible, containing distinct letters,
- each taken only once - coming from s1 or s2.

# Examples:
```
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```
"""

def longest_distinct_sorted_string(s1: str, s2: str) -> str:
    return ''.join(sorted(set(s1 + s2)))