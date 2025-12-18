"""
QUESTION:
Implement a function `hash_function` that takes a 32-bit integer `h` and returns the result of a hash function applied to `h`. The hash function consists of two operations: 

1. Multiply `h` by `0x85ebca6b`, perform a bitwise AND with `0xFFFFFFFF` to ensure the result remains within the 32-bit range.
2. XOR the result from step 1 with a right shift of `h` by 13 bits.

The function should return the final hashed value of `h`. The function signature is `def hash_function(h: int) -> int:`
"""

def hash_function(h: int) -> int:
    h = (h * 0x85ebca6b) & 0xFFFFFFFF  
    h ^= h >> 13  
    return h