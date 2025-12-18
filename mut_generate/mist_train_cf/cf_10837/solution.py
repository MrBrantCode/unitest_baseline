"""
QUESTION:
Implement a function named `huffman_decompress` that takes two parameters: a compressed string and a dictionary containing Huffman codes, and returns the decompressed string. The function should correctly decompress the compressed string using the provided Huffman codes. The Huffman codes dictionary maps each character to its corresponding Huffman code.
"""

def huffman_decompress(compressed_string, huffman_codes):
    decompressed_string = ''
    code = ''
    huffman_codes = {value: key for key, value in huffman_codes.items()}
    for bit in compressed_string:
        code += bit
        if code in huffman_codes:
            decompressed_string += huffman_codes[code]
            code = ''

    return decompressed_string