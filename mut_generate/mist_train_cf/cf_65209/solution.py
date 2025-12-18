"""
QUESTION:
Create a function `cycpattern_check(a, b)` that checks if string `b` or any of its rotations exist in a sequence within string `a`. The function should be case-insensitive, ignore special characters, and handle words with repeated characters. The function should return `True` if `b` or any of its rotations exist in `a` and `False` otherwise.
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

        # if rotated 'b' exists within the twice length 'a', return True
        if rotated_b in a_twice:
            return True

    # If after checking all rotations, 'b' is not found in 'a', return False
    return False