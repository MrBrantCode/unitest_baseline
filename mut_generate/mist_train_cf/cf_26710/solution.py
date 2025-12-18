"""
QUESTION:
Implement the `decode` function, which takes a byte string `core` as input. The function should return a new byte string obtained by replacing each byte in the input string with the byte that is the bitwise XOR of that byte and the next byte in the input string, leaving the last byte unchanged if the input string has an odd length.
"""

def decode(core: bytes) -> bytes:
    decoded_bytes = b''
    for i in range(len(core) - 1):
        decoded_bytes += bytes([core[i] ^ core[i + 1]])
    decoded_bytes += core[-1:]  # Append the last byte if the input length is odd
    return decoded_bytes