"""
QUESTION:
Implement a function `extract_hash_index(bitboard, magic)` that takes an occupancy bitboard and a magic number as input and returns the corresponding hash index. The function should calculate the hash index using the given occupancy bitboard and magic number, and return the result. The occupancy bitboard is represented as a bitarray, and the magic number is a precomputed constant. The function should use magic bit manipulation to efficiently map the occupancy bitboard to a hash index.
"""

def extract_hash_index(bitboard, magic):
    # Magic bit manipulation to extract hash index
    return (bitboard * magic) >> 60