"""
QUESTION:
Implement a function `calculate_digest` that takes in the string `S`, a positive integer `P`, a list of integers `v`, a positive integer `key_size`, a positive integer `u`, and a list of integers `D`. The function should calculate the digest `A` by performing the following steps:

- Concatenate the string `S` and the integer `P` to get the string `I`.
- Create a bytearray `B` from the list of integers `v`.
- Calculate `c` by dividing the sum of `key_size` and `u - 1` by `u`.
- Create a new SHA-256 digest and update it with the bytes of `D` and the string `I` for `c` iterations.

The function should return the final digest `A` as bytes.
"""

from typing import List
import hashlib

def calculate_digest(S: str, P: int, v: List[int], key_size: int, u: int, D: List[int]) -> bytes:
    I = S + str(P)
    B = bytearray(v)
    c = ((key_size + u - 1) // u)
    digest = hashlib.sha256()  
    for i in range(1, c + 1):
        digest.update(bytes(D))
        digest.update(I.encode('utf-8'))
    return digest.digest()