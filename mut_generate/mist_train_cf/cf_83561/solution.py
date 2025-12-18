"""
QUESTION:
Implement the function cycpattern_check that takes two strings a and b as parameters. The function should verify if string b or any of its rotational arrangements form a continuous subsequence within string a, ignoring case sensitivity and non-alphanumeric characters.
"""

def cycpattern_check(a, b):
    # Cleaning the strings: converting to lower case and removing unusual characters
    a = ''.join(e for e in a if e.isalnum()).lower()
    b = ''.join(e for e in b if e.isalnum()).lower()

    # Generating all possible rotational arrangements of b
    b_rotations = [b[i:] + b[:i] for i in range(len(b))]

    # Checking if any of the rotational arrangements of b form a part of a
    for b_rot in b_rotations:
        if b_rot in a:
            return True

    return False