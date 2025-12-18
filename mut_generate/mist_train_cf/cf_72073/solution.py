"""
QUESTION:
Write a function called `decode_cyclic` that takes an encoded string `s` as input and returns the decoded string. The encoded string was created by cycling sets of three-character groups, moving the first character to the end of each group. The function should handle single characters, empty spaces, and larger inputs efficiently.
"""

def decode_cyclic(s: str):
    """
    returns a decoded string, which was encoded using the above encode_cyclic function, tolerating stand-alone characters and empty spaces
    """
    # Splitting the given string into groups of at most 3 characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # For each group, if length is 3, reverse its cyclic rotation, else let it be
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)