"""
QUESTION:
Implement the `rail_fence(plaintext, n)` function, which takes a string `plaintext` and an integer `n` as input and returns the ciphertext generated using the rail fence cipher algorithm with `n` rails. The input plaintext contains only uppercase and lowercase letters, with no special characters or spaces. The function should handle cases where the length of the plaintext is not a multiple of `n`.
"""

def rail_fence(plaintext, n):
    plaintext_length = len(plaintext)
    line_size = -(-plaintext_length // n)  # Equivalent to int(np.ceil(plaintext_length/n))
    ciphertext = ""

    for i in range(n):
        for j in range(line_size):
            if j * n + i < plaintext_length:
                ciphertext += plaintext[j * n + i]

    return ciphertext