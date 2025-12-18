"""
QUESTION:
Create a function named `sophisticated_decrypt` that takes two parameters: an integer `cipher_integer` and an integer `divide_count`. The function should apply a decryption scheme to `cipher_integer` by shifting its binary representation to the right by `divide_count` positions. If `cipher_integer` is negative, the function should preserve its sign. If `cipher_integer` is zero, the function should return zero. Implement this decryption scheme using bitwise operations and ensure it handles both positive and negative integers.
"""

def sophisticated_decrypt(cipher_integer, divide_count):
    """
    Applies a decryption scheme to cipher_integer by shifting its binary representation 
    to the right by divide_count positions. Preserves the sign of cipher_integer if it's negative.
    If cipher_integer is zero, returns zero.
    """
    if cipher_integer == 0:
        return 0
    elif cipher_integer < 0:
        return -(-cipher_integer >> divide_count)
    else:
        return cipher_integer >> divide_count