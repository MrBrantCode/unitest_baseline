"""
QUESTION:
Implement a function `compress_string(input_str)` that takes a string `input_str` containing only uppercase letters as input. The function should return the compressed form of the input string using Run-Length Encoding (RLE), where consecutive identical elements are replaced with a count and a single instance of the element. If the compressed form is longer than the original string, the function should return the original string.
"""

def compress_string(input_str):
    compressed = ""
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed += str(count) + input_str[i - 1]
            count = 1
    compressed += str(count) + input_str[-1]

    return compressed if len(compressed) < len(input_str) else input_str