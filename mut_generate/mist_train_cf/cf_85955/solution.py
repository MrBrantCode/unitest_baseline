"""
QUESTION:
Create a function called `encrypt` that takes a string `s` and a Vigenère cipher table `table` as inputs. The function should use the first letter of the string as the primary key to the cipher and the last letter as a secondary key. The function should return the encrypted string. The input string `s` must be validated to ensure it is a lowercase string. If the input string is not valid, the function should return "Invalid input". The function should also check if the primary and secondary keys are present in the cipher table and if each character in the string is present in the corresponding sub-dictionaries of the cipher table. If any of these checks fail, the function should return an error message.
"""

def encrypt(s, table):
    if not s.isalpha() or not s.islower():
        return "Invalid input"

    key = s[0] if s else None
    secondary_cipher_key = s[-1] if s else None

    if not key or key not in table or not secondary_cipher_key or secondary_cipher_key not in table:
        return "Invalid key/cipher"

    encryption = ""
    for character in s:
        if character not in table[key] or character not in table[secondary_cipher_key]:
            return "Invalid character in string"
        encryption += table[key][character]
        encryption += table[secondary_cipher_key][character]
    return encryption