"""
QUESTION:
Implement a function `optimized_decrypt(cipher_text, known_part=None)` that takes a cipher text and an optional known part of the plain text as input and returns the decrypted text. The substitution key used for encryption is a simple one-to-one mapping of characters. The goal is to devise a more optimized algorithm to decrypt the cipher text in a shorter time than the brute-force approach.
"""

def entance(cipher_text, known_part=None):
    # Initialize a dictionary to store the mapping of encrypted characters to decrypted characters
    mapping = {}

    # If a known part of the plain text is provided, use it to populate the initial mapping
    if known_part:
        for i in range(len(known_part)):
            mapping[cipher_text[i]] = known_part[i]

    # Iterate through the cipher text to deduce the mapping of characters
    for i in range(len(cipher_text)):
        if cipher_text[i] not in mapping:
            # If the character is not already mapped, add it to the mapping with a placeholder value
            mapping[cipher_text[i]] = None

    # Perform frequency analysis on the cipher text to deduce the most common characters
    # and their likely mappings based on the frequency distribution in English language

    # Use the deduced mapping to decrypt the cipher text
    decrypted_text = ''.join(mapping[char] if mapping[char] else char for char in cipher_text)

    return decrypted_text