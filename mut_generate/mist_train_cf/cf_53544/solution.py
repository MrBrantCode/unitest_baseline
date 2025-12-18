"""
QUESTION:
Given an integer array `data` of length `1 <= data.length <= 2 * 10^4`, where each integer represents a byte of data and `0 <= data[i] <= 255`, write a function `validUtf8(data)` that returns `True` if the data is a valid UTF-8 encoding, `False` if the data is not a valid UTF-8 encoding due to invalid starting byte or incorrect number of continuation bytes, and a specific error message for invalid continuation byte. The function should validate UTF-8 encoded characters according to the following rules:
- A character in UTF-8 can be from 1 to 4 bytes long.
- For a 1-byte character, the first bit is a `0`, followed by its Unicode code.
- For an n-bytes character, the first `n` bits are all one's, the `n + 1` bit is `0`, followed by `n - 1` bytes with the most significant `2` bits being `10`.
"""

def validUtf8(data):
    sz = 0
    for num in data:
        if sz == 0:
            if (num >> 5) == 0b110: sz = 1
            elif (num >> 4) == 0b1110: sz = 2
            elif (num >> 3) == 0b11110: sz = 3
            elif (num >> 7): return False
        else:
            if (num >> 6) != 0b10: 
                return "Error: Invalid continuation byte"
            sz -= 1
    return sz == 0