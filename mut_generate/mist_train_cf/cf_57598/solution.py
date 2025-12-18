"""
QUESTION:
Create a function named `decode_string(s)` that takes a string `s` as input and returns the decoded string by replacing characters based on the `decoding_cipher` dictionary. The function should handle potential errors, including non-string input and characters not defined in the dictionary. If an error occurs, the function should print the error message and return `None`. The decoding_cipher dictionary is: `{"x" : "a", "y": "b", "z" : "c"}`.
"""

def decode_string(s):
    decoding_cipher = {"x" : "a", "y": "b", "z" : "c"}
    try:
        assert isinstance(s, str), "Input must be a string"
        decoded_s = "".join([decoding_cipher[char] if char in decoding_cipher else char for char in s])
    except Exception as e:
        print("Error occurred:", e)
        return None
    return decoded_s