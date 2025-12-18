"""
QUESTION:
Implement a function `reverse_block(block: bytearray) -> None` that reverses the order of the 32-bit unsigned integers in the given bytearray `block` in place. The function should use the provided `w_get` and `w_set` functions to access and modify the integers in the `block`, without using any additional data structures or libraries.
"""

def w_get(index, block):
    """Fetches the 32-bit unsigned integer from the block at the given index."""
    return struct.unpack('>I', block[index*4:index*4+4])[0]

def w_set(index, value, block):
    """Sets the 32-bit unsigned integer in the block at the given index."""
    block[index*4:index*4+4] = struct.pack('>I', value)

def reverse_block(block: bytearray) -> None:
    """Reverses the order of the 32-bit unsigned integers in the given bytearray block in place."""
    # Calculate the number of 32-bit unsigned integers in the block
    num_integers = len(block) // 4

    # Iterate through half of the block and swap the integers
    for i in range(num_integers // 2):
        # Fetch the integers from both ends of the block
        left_integer = w_get(i, block)
        right_integer = w_get(num_integers - i - 1, block)

        # Swap the integers in the block
        w_set(i, right_integer, block)
        w_set(num_integers - i - 1, left_integer, block)