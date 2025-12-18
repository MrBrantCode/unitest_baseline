"""
QUESTION:
Create a hash function in Python that can efficiently store and retrieve a large repository of words with minimal collisions. The function should take a string key and the size of the hash table as input and return a valid index for the hash table. The hash function should be designed to distribute keys uniformly and minimize collisions. Implement a collision resolution method such as chaining or open addressing.
"""

def hash_function(key_str, size):
    return sum([ord(c) for c in key_str]) % size