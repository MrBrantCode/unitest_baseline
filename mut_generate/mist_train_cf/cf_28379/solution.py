"""
QUESTION:
You are tasked with simulating the initial block download (IBD) phase of a blockchain, where a node receives and processes blocks out of order. Implement a function `process_blocks(blocks, threshold)` that takes a list of blocks with their heights and chainwork values, and a minimum chainwork threshold. The function should return the block height at which the total chainwork of the received blocks exceeds the threshold. Assume the blocks may arrive out of order and must be processed in chronological order based on their timestamps.
"""

def process_blocks(blocks, threshold):
    chainwork = 0
    max_height = 0

    for block in sorted(blocks, key=lambda x: x["timestamp"]):
        chainwork += block["chainwork"]
        if chainwork >= threshold:
            max_height = max(max_height, block["height"])

    return max_height