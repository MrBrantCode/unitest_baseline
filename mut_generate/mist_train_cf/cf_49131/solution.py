"""
QUESTION:
You are given an encoded string `S` and an index `K`. The encoded string is decoded by reading it one character at a time and following these steps: 
- If the character is a letter, it is written onto the tape.
- If the character is a digit `d`, the entire current tape is repeated `d-1` more times.
- If the character is a special character `#`, the last character written on the tape is removed.
Return the `K`-th letter (1-indexed) in the decoded string.

Constraints: 
- `3 <= S.length <= 100`
- `S` contains only lowercase letters, digits `2` through `9`, and the special character `#`.
- `S` starts with a letter.
- `1 <= K <= 10^9`
- `K` is less than or equal to the length of the decoded string.
- The decoded string has less than `2^63` letters.
"""

def entrance(S, K):
    size = 0
    # Calculate the total length of the string
    for char in S:
        if char.isdigit():
            size *= int(char)
        elif char.isalpha():
            size += 1
        elif char == '#':
            if size == 0: size += 1
            else: size -= 1
    # Start from the end of S
    for char in reversed(S):
        K %= size
        if K == 0 and char.isalpha():
            return char
        if char.isdigit():
            size /= int(char)
        elif char.isalpha():
            size -= 1
        elif char == '#':
            if size != 0: size += 1
            else: size -= 1