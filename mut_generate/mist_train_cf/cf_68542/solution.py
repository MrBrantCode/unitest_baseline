"""
QUESTION:
Implement the `encode_cyclic` and `decode_cyclic` functions to handle a string input that may include UTF-8 encoded unusual characters, numeric quantities, punctuation markings, Unicode symbols, and whitespace. The `encode_cyclic` function should convert the input string into a list of representing Unicode code points with a cyclic displacement of 4 and encode the result using base64. The `decode_cyclic` function should reverse this process to retrieve the original string. The cyclic displacement should be applied to all characters, not just alphabet characters and spaces.
"""

import base64

def encode_cyclic(s: str) -> str:
    """
    Promptly conveys an encoded string following a cyclic displacement on clusters of four constituents, involving numerics, punctuation indications and Unicode symbols.
    """
    # convert string to list of representing Unicode code points
    lst = [ord(c) for c in s]
    for i in range(len(lst)):
        lst[i] += i % 4  # cyclic shift
    res = ''.join(chr(i) for i in lst)
    res = res.encode("utf-8")  # encode to utf-8 to handle special characters
    return base64.b64encode(res).decode("utf-8")  # encode using base64 for further protection

def decode_cyclic(s: str) -> str:
    """
    Give back the decoded string derived from encode_cyclic operation, managing UTF-8 encoded peculiar symbols, numeric figures, punctuation signs, Unicode symbols and negligible features like whitespace.
    """
    s = base64.b64decode(s).decode("utf-8")  # decode using base64
    lst = [ord(c) for c in s]
    for i in range(len(lst)):
        lst[i] -= i % 4  # cyclic shift
    return ''.join(chr(i) for i in lst)