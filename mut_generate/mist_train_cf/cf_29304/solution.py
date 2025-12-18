"""
QUESTION:
Implement a function `simulate_crypto_operation(cipher_blocks: List[bytes], BLOCK_SIZE: int) -> bytes` that simulates a cryptographic operation on a list of cipher blocks. The function should take a list of cipher blocks `cipher_blocks` and the `BLOCK_SIZE` as input and return the final manipulated `probe` byte array after simulating the operation. The function should perform the following operations: initialize two byte arrays `delta1` and `delta2` with zeros, iterate over the `BLOCK_SIZE` to manipulate `delta2`, perform bitwise XOR operations on byte arrays to update `probe`, and return the final `probe` byte array.
"""

from typing import List

def entrance(cipher_blocks: List[bytes], BLOCK_SIZE: int) -> bytes:
    probeBlocks = cipher_blocks.copy()
    delta1 = bytearray([0] * BLOCK_SIZE)
    delta2 = bytearray([0] * BLOCK_SIZE)

    for i in range(BLOCK_SIZE):
        for j in range(BLOCK_SIZE - i):
            delta2[BLOCK_SIZE - (1 + j)] = (BLOCK_SIZE - i)

        for j in range(256):
            cipherInter = probeBlocks.copy()
            delta2[i] = j
            delta = bytearray(bytes([a ^ b for (a,b) in zip(delta1, delta2)]))

            block = cipherInter[len(cipherInter) - 2]
            probe = bytearray(bytes([a ^ b for (a,b) in zip(block, delta)]))

    return bytes(probe)