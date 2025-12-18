"""
QUESTION:
Write a function called `calculate_virtual_address` that takes two 16-bit integer arguments, a segment register value and an offset register value, and returns their combined 20-bit virtual memory address. The function should combine the two values by shifting the segment register 4 bits to the left and adding it to the offset register. The inputs and output should be represented as hexadecimal values.
"""

def calculate_virtual_address(segment, offset):
    """
    Calculate the 20-bit virtual memory address from a 16-bit segment register value and a 16-bit offset register value.

    The function combines the two values by shifting the segment register 4 bits to the left and adding it to the offset register.

    Args:
        segment (int): A 16-bit integer representing the segment register value.
        offset (int): A 16-bit integer representing the offset register value.

    Returns:
        int: The combined 20-bit virtual memory address as a hexadecimal value.
    """
    virtual_address = (segment << 4) + offset
    return virtual_address