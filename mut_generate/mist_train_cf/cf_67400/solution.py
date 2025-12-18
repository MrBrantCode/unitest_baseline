"""
QUESTION:
Create a function named `descending_squares_hashed_values` that takes a list of integers and a string hash algorithm type as input. The function should calculate squares of each number, compute their hash values using the given hash algorithm, and return a dictionary where keys are the original numbers and values are their hashed square values, sorted in descending order based on the hexadecimal values of the hashes. The hash algorithm type should support 'md5', 'sha1', 'sha224', 'sha256', 'sha384', and 'sha512'.
"""

import hashlib

def descending_squares_hashed_values(numbers: list, hash_type: str):
    """Return a dictionary with original numbers as keys and their squared values' hashed values, ordered by 
    the hexadecimal representation of the hash value.
    """

    hash_dict={}

    for num in numbers:
        sqr_num=str(num**2).encode('utf-8')
        if hash_type=='md5':
            hasher=hashlib.md5()
        elif hash_type=='sha1':
            hasher=hashlib.sha1()
        elif hash_type=='sha224':
            hasher=hashlib.sha224()
        elif hash_type=='sha256':
            hasher=hashlib.sha256()
        elif hash_type=='sha384':
            hasher=hashlib.sha384()
        elif hash_type=='sha512':
            hasher=hashlib.sha512()
        else:
            continue
        hasher.update(sqr_num)
        hash_dict[num]=hasher.hexdigest()

    return {k: v for k, v in sorted(hash_dict.items(), key=lambda item: item[1], reverse=True)}