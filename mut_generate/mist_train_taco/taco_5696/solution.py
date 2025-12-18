"""
QUESTION:
Given a number, write a function to output its reverse digits.  (e.g. given 123 the answer is 321)


Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

### Examples
```
 123 ->  321
-456 -> -654
1000 ->    1
```
"""

def reverse_digits(n: int) -> int:
    s = str(n)
    if s[0] == '-':
        reversed_str = '-' + s[:0:-1]
    else:
        reversed_str = s[::-1]
    return int(reversed_str)