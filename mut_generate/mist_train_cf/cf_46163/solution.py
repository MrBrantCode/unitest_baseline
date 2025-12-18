"""
QUESTION:
Create a function called `encode_string` that takes a string `text` as input and returns a new string where each character's Unicode value has been incremented by 2. The function should handle any type of character, including special characters and numerals, and should raise an exception if an error occurs. The output string should be a concatenation of the transformed characters.
"""

def encode_string(text):
    try: 
        return ''.join(chr(ord(ch) + 2) for ch in text)
    except Exception as err:
        print(f"Error: {err}")