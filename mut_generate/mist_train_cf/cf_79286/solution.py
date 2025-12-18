"""
QUESTION:
Write a function named `calculate_hashes` that takes a string input and returns its MD5, SHA1, SHA256, and SHA512 hashes in both hexadecimal and Base64 encoded strings. The input string must be first encoded to bytes before hashing. Use the hashlib library for hashing and base64 library for encoding.
"""

import hashlib
import base64

def calculate_hashes(input_string):
    """
    Calculate MD5, SHA1, SHA256, and SHA512 hashes of the input string in both hexadecimal and Base64 encoded strings.
    
    Args:
        input_string (str): The input string to be hashed.

    Returns:
        dict: A dictionary containing the MD5, SHA1, SHA256, and SHA512 hashes in hexadecimal and Base64 encoded strings.
    """
    # encode string to bytes
    byte_string = input_string.encode()

    # create hash objects
    sha256_obj = hashlib.sha256(byte_string)
    md5_obj = hashlib.md5(byte_string)
    sha1_obj = hashlib.sha1(byte_string)
    sha512_obj = hashlib.sha512(byte_string)

    # get hash hexadecimal strings
    sha256_hex = sha256_obj.hexdigest()
    md5_hex = md5_obj.hexdigest()
    sha1_hex = sha1_obj.hexdigest()
    sha512_hex = sha512_obj.hexdigest()

    # encode the hexadecimal hash values using base64
    sha256_b64 = base64.b64encode(sha256_obj.digest()).decode('utf-8')
    md5_b64 = base64.b64encode(md5_obj.digest()).decode('utf-8')
    sha1_b64 = base64.b64encode(sha1_obj.digest()).decode('utf-8')
    sha512_b64 = base64.b64encode(sha512_obj.digest()).decode('utf-8')

    return {
        "MD5": {"hex": md5_hex, "base64": md5_b64},
        "SHA1": {"hex": sha1_hex, "base64": sha1_b64},
        "SHA256": {"hex": sha256_hex, "base64": sha256_b64},
        "SHA512": {"hex": sha512_hex, "base64": sha512_b64}
    }