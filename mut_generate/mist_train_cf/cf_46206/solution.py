"""
QUESTION:
Create two functions, `encrypt(string, key, Vigenère_cipher_table)` and `decrypt(ciphertext, key, Vigenère_cipher_table)`, that implement a Vigenère cipher encryption and decryption. The `encrypt` function should take a string, a key, and a Vigenère cipher table as input and return the encrypted string. The `decrypt` function should take the encrypted string, the same key, and the Vigenère cipher table as input and return the decrypted string.

The Vigenère cipher table is a dictionary of dictionaries where each inner dictionary maps plaintext characters to ciphertext characters. The key parameter is used to select the inner dictionary from the table. If the key or a character in the string is not found in the table, the functions should print an error message and return None.
"""

def entance(string, key, Vigenere_cipher_table, mode):
    try:
        result = ""
        if mode == "encrypt":
            for i in string:
                result += Vigenere_cipher_table[key][i]
        elif mode == "decrypt":
            for cipherchar in string:
                for char in Vigenere_cipher_table[key]:
                    if Vigenere_cipher_table[key][char] == cipherchar:
                        result += char
                        break
        else:
            print("Invalid mode. Use 'encrypt' or 'decrypt'.")
            return None
    except KeyError:
        print("Invalid key or character not defined in the cipher table")
        return None
    return result