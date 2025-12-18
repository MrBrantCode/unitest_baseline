"""
QUESTION:
Write two functions, `encode_cyclic` and `decode_cyclic`. The function `encode_cyclic(z: str)` takes a string `z` as input, divides it into groups of three characters, cycles each group, and returns the encoded string. The function `decode_cyclic(s: str)` takes a string `s` as input, which is encoded by the `encode_cyclic` function, decodes the string, and returns the original string. The decoding should handle singular characters, empty spaces, and punctuation correctly.
"""

def encode_cyclic(z: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    groups = [z[3 * i:min(3 * i + 3, len(z))] for i in range((len(z) + 2) // 3)]
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Should handle a string encoded with the encode_cyclic function and return the decoded string,
    managing singular characters, empty spaces, and punctuation.
    """
    groups = [s[3 * i:min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]

    return "".join(groups)