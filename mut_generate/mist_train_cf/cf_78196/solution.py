"""
QUESTION:
Create a function `create_hash_table(n)` that takes an integer `n` as input and returns a dictionary with `n` key-value pairs. The keys should be English lowercase letters starting from 'a' and the corresponding values should start from 1, incrementing by 1. The function should validate the input to ensure `n` is within the range 1 to 26 (inclusive). If `n` is outside this range, return an error message. Additionally, implement an interactive function `search_key(dictionary, key)` that takes a dictionary and a key as input, returns the value associated with the key, and handles the case when the key is not in the dictionary.
"""

def entrance(n):
    """Create a hash table with n number of key-value pairs"""
    if 1<=n<=26:
        return {chr(97+i): i+1 for i in range(n)}
    else:
        return "Error: The number provided is not in the acceptable range (1≤n≤26)"

def search_key(dictionary, key):
    """Find the value of a given key from the hash table"""
    return dictionary.get(key, "Error: The provided key is not in the table!")