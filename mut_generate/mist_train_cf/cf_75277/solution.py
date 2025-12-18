"""
QUESTION:
Create a function `encrypt_Vigenere(s, table)` that encrypts a given string `s` based on a provided Vigenère cipher table `table`. The function should use the first letter of the string `s` as the key to the cipher. Assume that `table` and `s` only contain lowercase letters and `s` is not empty.
"""

def encrypt_Vigenere(s, table):
    """
    Encrypts a given string s based on a provided Vigenère cipher table.
    
    Parameters:
    s (str): The input string to be encrypted.
    table (dict): The Vigenère cipher table.
    
    Returns:
    str: The encrypted string.
    """
    key = s[0]
    encrypted_string = ''
    for i in range(1, len(s)):
        encrypted_string += table[key][s[i]]
    return encrypted_string