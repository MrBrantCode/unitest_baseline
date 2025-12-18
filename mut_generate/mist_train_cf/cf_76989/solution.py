"""
QUESTION:
Given an integer array `data` representing bytes of a UTF-8 encoding, determine if it is a valid UTF-8 sequence. Each integer in `data` represents a byte, and only the least significant 8 bits are used. A valid UTF-8 sequence follows these rules: 
- A character can be 1 to 4 bytes long.
- For a 1-byte character, the first bit is `0`, followed by its Unicode code.
- For an n-byte character, the first `n` bits are all one's, the `n + 1` bit is `0`, followed by `n - 1` bytes with the most significant `2` bits being `10`.

Implement the `validUtf8` function that returns `True` if `data` is a valid UTF-8 sequence and `False` otherwise. The input array `data` has a length between 1 and 2 * 10^4, and each integer in `data` is between 0 and 255.
"""

def validUtf8(data):
    count = 0   
    mask1 = 1 << 7   
    mask2 = 1 << 6   
    for byte in data:
        mask = 1 << 7
        if count == 0:  
            while mask & byte:   
                count += 1
                mask = mask >> 1
            if count == 0:   
                continue
            if count > 4 or count == 1:   
                return False  
        else:  
            if not (byte & mask1 and not (byte & mask2)): 
                return False
        count -= 1
    return count == 0