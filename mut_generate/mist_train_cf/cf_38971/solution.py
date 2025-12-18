"""
QUESTION:
Implement a function named `detect_aes_ecb` that takes a given ciphertext as input and returns `True` if the ciphertext appears to have been encrypted using AES in ECB mode, and `False` otherwise. The input ciphertext is a string of bytes and is a multiple of 16 bytes in length. Assume the presence of duplicate 16-byte blocks indicates ECB mode.
"""

def detect_aes_ecb(ciphertext):
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    unique_blocks = set(blocks)
    return len(blocks) != len(unique_blocks)