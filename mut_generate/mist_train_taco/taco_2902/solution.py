"""
QUESTION:
You have been recruited by an unknown organization for your cipher encrypting/decrypting skills.  
Being new to the organization they decide to test your skills.  
Your first test is to write an algorithm that encrypts the given string in the following steps.

1. The first step of the encryption is a standard ROT13 cipher.
This is a special case of the caesar cipher where the letter is encrypted with its key that is thirteen letters down the alphabet,  
i.e. `A => N, B => O, C => P, etc..`

1. Part two of the encryption is to take the ROT13 output and replace each letter with its exact opposite. `A => Z, B => Y, C => X`.  
The return value of this should be the encrypted message.


Do not worry about capitalization or punctuation. All encrypted messages should be lower case and punctuation free.  
As an example, the string `"welcome to our organization"` should return `"qibkyai ty ysv yvgmzenmteyz"`.

Good luck, and congratulations on the new position.
"""

def encrypt_message(message: str) -> str:
    """
    Encrypts the given message using a two-step encryption process:
    1. Apply a ROT13 cipher.
    2. Replace each letter with its exact opposite in the alphabet.

    Parameters:
    - message (str): The message to be encrypted. Should be lowercase and punctuation-free.

    Returns:
    - str: The encrypted message.
    """
    def rot13(c: str) -> str:
        """Applies ROT13 cipher to a single character."""
        if c.isalpha():
            return chr((ord(c) - 97 + 13) % 26 + 97)
        return c
    
    def opposite_letter(c: str) -> str:
        """Replaces a letter with its exact opposite in the alphabet."""
        if c.isalpha():
            return chr(122 - (ord(c) - 97))
        return c
    
    # Step 1: Apply ROT13 cipher
    rot13_message = ''.join(rot13(c) for c in message)
    
    # Step 2: Replace each letter with its exact opposite
    encrypted_message = ''.join(opposite_letter(c) for c in rot13_message)
    
    return encrypted_message