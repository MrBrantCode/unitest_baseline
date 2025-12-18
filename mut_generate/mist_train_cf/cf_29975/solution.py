"""
QUESTION:
Implement a function `encode_mask_results` that takes a string `s` and a list of integers `mask` as input. The function should return the encoded string by shifting each character in `s` by the corresponding amount specified in `mask`. If the end of `s` is reached during shifting, the process wraps around to the beginning of `s`. The shift should be performed within the alphabet (i.e., 'a' to 'z'), and the wrapping should occur when a shift goes beyond 'z' or before 'a'.
"""

from typing import List

def encode_mask_results(s: str, mask: List[int]) -> str:
    encoded = ''
    for i in range(len(s)):
        shift = mask[i % len(mask)]  # Use modulo to cycle through the mask
        encoded += chr((ord(s[i]) - 97 + shift) % 26 + 97)  # Shift the character and wrap around if needed
    return encoded