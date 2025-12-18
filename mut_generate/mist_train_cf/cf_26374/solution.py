"""
QUESTION:
Implement a function named `getDigest` that takes two parameters: an input string and a hashing algorithm name. The function should support at least three hashing algorithms: MD5, SHA-256, and SHA-512. It should calculate the digest of the input string using the specified algorithm and return a dictionary containing the algorithm name and the hexadecimal digest. If an unsupported algorithm is provided, the function should return an error message.
"""

import hashlib

def getDigest(input, algorithm):
    algorithms = {
        'md5': hashlib.md5,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }

    if algorithm.lower() not in algorithms:
        return "Invalid algorithm"

    hash_algorithm = algorithms[algorithm.lower()]()
    hash_algorithm.update(input.encode('utf-8'))
    digest = hash_algorithm.hexdigest()

    return {'algorithm': algorithm, 'digest': digest}