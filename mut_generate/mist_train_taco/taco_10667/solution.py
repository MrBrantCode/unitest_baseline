"""
QUESTION:
Given 2 strings, `a` and `b`, return a string of the form short+long+short, with the shorter string on the outside
and the longer string on the inside. The strings will not be the same length, but they may be empty ( length `0` ).

For example:

```python
solution("1", "22") # returns "1221"
solution("22", "1") # returns "1221"
```
"""

def concat_short_long_short(a, b):
    return a + b + a if len(a) < len(b) else b + a + b