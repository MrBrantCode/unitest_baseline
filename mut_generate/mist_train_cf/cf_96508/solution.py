"""
QUESTION:
Generate a URL-encoded token of 128 characters based on a randomly generated seed using the SHA-3 algorithm. The token should be generated using a variant of SHA-3 that produces a hash of sufficient length (SHA3-256, SHA3-384, or SHA3-512) and then truncated to 128 characters. Implement this in Python using the hashlib and urllib.parse libraries.
"""

import hashlib
import urllib.parse

def generate_token(seed):
    # Hash the seed using SHA-3 (SHA3-256 in this example)
    hashed_seed = hashlib.sha3_256(seed.encode()).hexdigest()
    
    # Convert the hash into a 128-character hexadecimal string
    token = hashed_seed[:128]
    
    # Apply URL encoding to the token
    encoded_token = urllib.parse.quote(token)
    
    return encoded_token