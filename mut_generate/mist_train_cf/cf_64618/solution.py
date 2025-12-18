"""
QUESTION:
Create two functions: `string_to_bytes` and `bytes_to_string`. The `string_to_bytes` function should take a string input, split it into words, and transform each word into a bytes array, forming a 2D array of bytes. The `bytes_to_string` function should reverse this process by taking a 2D array of bytes and converting it back to the original string. The functions should work with any printable ASCII characters and handle spaces between words correctly. 

Restrictions: The input string does not have leading or trailing whitespaces and words are separated by a single space.
"""

def entrance(inp_string):
    split_str = inp_string.split(' ')
    bytes_2D = [[byte for byte in word.encode()] for word in split_str]
    decoded_words = [bytes(word).decode() for word in bytes_2D]
    return ' '.join(decoded_words)