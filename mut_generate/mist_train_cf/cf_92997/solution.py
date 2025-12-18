"""
QUESTION:
Create a function named `hash_code` that takes a string key as input, generates a hash code using the MD5 hashing algorithm, and returns the hash code modulo 10^6. 

Create another function named `insert` that takes a hash table, a string key, and a string value as input. The function should calculate the hash code for the key using the `hash_code` function, and insert the key-value pair into the hash table at the calculated hash code index. 

The hash table should be of size 10^6, and the `insert` function should be used to insert 10^5 key-value pairs into the hash table.
"""

import hashlib

def hash_code(key):
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % (10**6)

def insert(hashtable, key, value):
    hash_value = hash_code(key)
    hashtable[hash_value] = value