"""
QUESTION:
Given a string `S` and an integer `K`, find and return the `K`-th letter (1-indexed) in the decoded string `S`. The string `S` is decoded according to the following rules:
- If the character read is a letter, that letter is written onto the tape.
- If the character read is a digit `d`, the entire current tape is repeatedly written `d-1` more times in total.
- If the character read is a special character `#`, the last character written on the tape is removed.
- If the character read is a special character `@`, the entire current tape is reversed.

The function should be named `decodeAtIndex` and should take `S` and `K` as inputs. The function should return the `K`-th letter in the decoded string. 

Constraints: 
- `3 <= len(S) <= 100`
- `S` will only contain lowercase letters, digits `2` through `9`, and the special characters `#` and `@`.
- `S` starts with a letter.
- `1 <= K <= 10^9`
- `K` is less than or equal to the length of the decoded string.
- The decoded string has less than `2^63` letters.
"""

def decodeAtIndex(s, K):
    size = 0
    for c in s:
        if c.isdigit():
            size *= int(c)
        elif c == "#":
            size -= 1
        elif c == "@":
            continue
        else:
            size += 1
    # Apply operations from last to first (reversed)
    for c in reversed(s):
        K %= size
        if K == 0 and c.isalpha():
            return c
        if c.isdigit():
            size /= int(c)
        elif c == "#":
            size += 1
        elif c == "@":
            continue
        else:
            size -= 1