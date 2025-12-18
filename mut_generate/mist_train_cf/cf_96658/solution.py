"""
QUESTION:
Implement a function `compare_strings(a, b)` that compares two input strings lexicographically based on their Unicode values. The function should return 0 if the strings are identical, 1 if `a` is greater than `b`, and -1 if `b` is greater than `a`. The comparison should ignore any whitespace characters in the middle of the strings, handle leading and trailing whitespace characters, and have a time complexity of O(n), where n is the length of the longer string.
"""

def compare_strings(a, b):
    a = a.strip()
    b = b.strip()

    pointer_a = 0
    pointer_b = 0

    while pointer_a < len(a) and pointer_b < len(b):
        char_a = a[pointer_a]
        char_b = b[pointer_b]

        if char_a.isspace():
            pointer_a += 1
            continue
        if char_b.isspace():
            pointer_b += 1
            continue

        if char_a != char_b:
            if ord(char_a) > ord(char_b):
                return 1
            else:
                return -1

        pointer_a += 1
        pointer_b += 1

    if pointer_a < len(a):
        return 1
    elif pointer_b < len(b):
        return -1
    else:
        return 0