"""
QUESTION:
Create a function named `huffman_decompress` that takes two parameters, `compressed_string` and `huffman_codes`, and returns the decompressed string using the provided Huffman codes. The function should correctly decompress the string even when the code being formed does not match any of the existing Huffman codes. The `huffman_codes` parameter is a dictionary where keys are characters and values are their corresponding Huffman codes.
"""

def huffman_decompress(compressed_string, huffman_codes):
    """
    Decompress a string using the provided Huffman codes.

    Args:
        compressed_string (str): The string to be decompressed.
        huffman_codes (dict): A dictionary where keys are characters and values are their corresponding Huffman codes.

    Returns:
        str: The decompressed string.
    """
    # Reverse the huffman_codes dictionary to map codes to characters
    reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}

    decompressed_string = ''
    code = ''
    for bit in compressed_string:
        code += bit
        if code in reverse_huffman_codes:
            decompressed_string += reverse_huffman_codes[code]
            code = ''
        elif any(code.startswith(code_val) for code_val in huffman_codes.values()) == False:
            # The code doesn't match any existing codes, so it's not a valid huffman code.
            # We need to keep reading more bits until we find a valid huffman code.
            continue

    return decompressed_string