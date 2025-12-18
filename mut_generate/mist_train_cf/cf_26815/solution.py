"""
QUESTION:
Write a function `find_original_message` that takes a string `stringKey` and a hashed message `hashedMessage` as input. The function should return the original message that matches the hashed message by generating all possible permutations of the characters in `stringKey`, hashing each permutation using MD5 hashing algorithm, and comparing it with `hashedMessage`. If no match is found, return "Message not found".
"""

import itertools
import hashlib

def find_original_message(stringKey: str, hashedMessage: str) -> str:
    for i in range(1, len(stringKey) + 1):
        for item in itertools.permutations(stringKey, i):
            message = ''.join(item)
            hashed = hashlib.md5(message.encode()).hexdigest()
            if hashed == hashedMessage:
                return message
    return "Message not found"