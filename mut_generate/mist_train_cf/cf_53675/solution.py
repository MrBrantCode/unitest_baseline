"""
QUESTION:
Create a function `cycpattern_check(a, b)` that takes two strings `a` and `b` as input and returns `True` if `b` is a cyclic permutation of a substring in `a`, and `False` otherwise. The function should ignore non-alphanumeric characters and be case-insensitive. The function should also return `False` if the length of `b` is greater than the length of `a`.
"""

def cycpattern_check(a, b):
    # Remove special characters and change to lowercase
    a_clean = ''.join(e for e in a if e.isalnum()).lower()
    b_clean = ''.join(e for e in b if e.isalnum()).lower()

    # Check if the length of 'b' is greater than 'a'. If yes, then it's impossible for 'b' to be in 'a'
    if len(b_clean) > len(a_clean):
        return False

    # With the cleaned versions, create a string which is twice as long as 'a' to accommodate for cyclic rotations
    a_twice = a_clean + a_clean

    # Check for all cyclic permutations
    for i in range(len(b_clean)):
        # Obtain a cyclic permutation of 'b'
        rotated_b = b_clean[i:] + b_clean[:i]

        # If rotated 'b' exists within the twice length 'a', return True
        if rotated_b in a_twice:
            return True

    # If after checking all rotations, 'b' is not found in 'a', return False
    return False