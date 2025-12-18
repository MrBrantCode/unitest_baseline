"""
QUESTION:
Write a Python function `calculate_block_hash` that takes a block's index, timestamp, data, and previous hash as input, and returns the hash of the block. The hash should be calculated using the SHA-256 algorithm and should be based on a JSON representation of the block's data. The block's data should include its index, timestamp, data, and previous hash.

The input parameters to the `calculate_block_hash` function should be as follows:
- `index`: the index of the block
- `timestamp`: the timestamp of the block
- `data`: the data stored in the block
- `previous_hash`: the hash of the previous block in the chain

The `calculate_block_hash` function should return the hash of the block as a hexadecimal string.
"""

import hashlib
import json

def calculate_block_hash(index, timestamp, data, previous_hash):
    block_string = json.dumps({"index": index, "timestamp": timestamp, "data": data, "previous_hash": previous_hash}, sort_keys=True)
    return hashlib.sha256(block_string.encode()).hexdigest()