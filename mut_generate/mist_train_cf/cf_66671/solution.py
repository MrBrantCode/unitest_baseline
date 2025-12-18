"""
QUESTION:
Create a function `decode_text(text)` that deciphers a given string employing a custom decoding algorithm. The algorithm should handle both lowercase and uppercase letters, as well as punctuation and numbers. The decoding rules are provided in the `decoding_cipher` dictionary, which maps characters to their decoded equivalents. The function should be optimized for handling large text strings.
"""

def decode_text(text):
    decoding_cipher = {
        "x" : "a", "y": "b", "z" : "c", 
        "X" : "A", "Y": "B", "Z" : "C", 
        "1" : "0", "2": "1", "3" : "2",
        "?": ".", "!": ",", ".": "!"
    }

    trans_table = str.maketrans(decoding_cipher)
    decoded_text = text.translate(trans_table)
    return decoded_text