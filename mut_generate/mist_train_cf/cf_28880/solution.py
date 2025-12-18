"""
QUESTION:
Implement a function `generate_round_keys(key)` that takes a 64-bit integer key as input and returns a list of 16 round keys, each represented as a tuple of two 28-bit integers. The function should perform the key schedule process of the AES algorithm to generate the round keys. The key schedule process involves splitting the original key into two 28-bit halves, and then for each round, performing a left shift on the halves based on a predefined shift schedule, combining the shifted halves, and applying a permutation operation to generate the round key.
"""

def generate_round_keys(key):
    # Initial permutation choice
    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    # Number of left shifts for each round
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    # Perform initial permutation choice (PC1)
    key = int(bin(key)[2:], 16)
    key = ''.join(format(key, '064b'))  # Convert to 64-bit binary string
    key = [key[i - 1] for i in pc1]  # Apply PC1 permutation

    # Split the key into two 28-bit halves
    c = key[:28]
    d = key[28:]

    round_keys = []

    # Generate round keys for each round
    for i in range(16):
        # Perform left shift on C and D
        c = c[shifts[i]:] + c[:shifts[i]]
        d = d[shifts[i]:] + d[:shifts[i]]

        # Combine C and D
        cd = c + d

        # Perform permutation choice 2 (PC2) to generate round key
        pc2 = [14, 17, 11, 24, 1, 5, 3, 28,
               15, 6, 21, 10, 23, 19, 12, 4,
               26, 8, 16, 7, 27, 20, 13, 2,
               41, 52, 31, 37, 47, 55, 30, 40,
               51, 45, 33, 48, 44, 49, 39, 56,
               34, 53, 46, 42, 50, 36, 29, 32]

        round_key = [cd[i - 1] for i in pc2]  # Apply PC2 permutation
        round_keys.append((int(''.join(round_key[:28]), 2), int(''.join(round_key[28:]), 2)))

    return round_keys