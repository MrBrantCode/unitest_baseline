"""
QUESTION:
Write a function called `decode_cyclic` that accepts a string `s` that has been encoded by shifting each group of three characters one position to the right. The function should reverse this encoding to return the original string. If a group has fewer than three characters, do not shift them.
"""

def decode_cyclic(s: str):
    """
    accepts a string encoded with a cyclic shift of three characters and returns the decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[-1:] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)