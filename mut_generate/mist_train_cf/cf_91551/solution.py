"""
QUESTION:
Implement a function `huffman_decompress(compressed_string, huffman_codes)` to decompress a string that was previously compressed using Huffman Coding. The function should take two parameters: `compressed_string` (the string to be decompressed) and `huffman_codes` (a dictionary containing the Huffman codes). The function should return the decompressed string.

The `huffman_codes` dictionary maps each character to its corresponding Huffman code. The `compressed_string` is a binary string containing the Huffman codes concatenated together. The decompression function should be able to correctly decompress the string by looking up the Huffman codes in the `huffman_codes` dictionary.
"""

def huffman_decompress(compressed_string, huffman_codes):
    """
    Decompress a string that was previously compressed using Huffman Coding.

    Parameters:
    compressed_string (str): The string to be decompressed.
    huffman_codes (dict): A dictionary containing the Huffman codes.

    Returns:
    str: The decompressed string.
    """
    decompressed_string = ''
    code = ''
    for bit in compressed_string:
        code += bit
        if code in huffman_codes.values():
            decompressed_string += list(huffman_codes.keys())[list(huffman_codes.values()).index(code)]
            code = ''

    return decompressed_string