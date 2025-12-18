"""
QUESTION:
Design a function `encrypt` that takes a string value as input, applies a custom encryption algorithm to the value, and returns the encrypted value. The encryption algorithm should ensure that the encrypted value is a valid string that can be decrypted back to its original value. Also, design a function `decrypt` that takes an encrypted string value as input and returns the original decrypted value. Use these functions to construct a JSON object with the encrypted "name" and "age" parameters and return the JSON object. The input parameters are a string "name" and an integer "age".
"""

def encrypt(value):
    # Custom encryption algorithm (you can replace this with your own)
    encrypted_value = value[::-1]  # reverse the string
    return encrypted_value

def decrypt(value):
    # Custom decryption algorithm (you need to implement the reverse process of encryption)
    decrypted_value = value[::-1]  # reverse the string back to original
    return decrypted_value

def entrance(name, age):
    # Encrypt the parameters
    encrypted_name = encrypt(name)
    encrypted_age = encrypt(str(age))

    # Construct the JSON object
    json_object = {
        "encrypted_name": encrypted_name,
        "encrypted_age": encrypted_age
    }
    return json_object