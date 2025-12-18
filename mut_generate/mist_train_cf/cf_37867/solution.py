"""
QUESTION:
Implement a function `calculate_function_hash(name)` that takes a string `name` representing the function name and returns the hash value calculated using a custom algorithm that involves bitwise operations and string manipulation, where the hash is calculated by iterating through the input string in segments of two characters, unpacking them into short integers, and applying the bitwise rotation operation `ror8(v) = ((v >> 8) & (2 ** 32 - 1)) | ((v << 24) & (2 ** 32 - 1))`. The function should return the resulting hash value.
"""

import struct

def ror8(v):
    return ((v >> 8) & (2 ** 32 - 1)) | ((v << 24) & (2 ** 32 - 1))

def calculate_function_hash(name):
    function_hash = 0
    for segment in [s for s in [name[i:i + 2] for i in range(len(name))] if len(s) == 2]:
        partial_name_short = struct.unpack('<H', segment.encode())[0]
        function_hash ^= partial_name_short + ror8(function_hash)
    return function_hash