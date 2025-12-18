"""
QUESTION:
Design a memory address decoder that takes three 8-bit input signals (`page_address`, `column_address`, `address`) and produces two control signals (`row_select`, `column_select`) to access a memory location in a 32x8 memory array. The `row_select` signal should be 5 bits long and the `column_select` signal should be 3 bits long.
"""

def decode_memory_address(page_address, column_address, address):
    """
    Decodes memory address into row and column select signals.

    Args:
        page_address (list): 8-bit page address signal.
        column_address (list): 8-bit column address signal.
        address (list): 8-bit address signal.

    Returns:
        tuple: A tuple containing the row select signal (5 bits) and column select signal (3 bits).
    """
    row_select = [page_address[2], page_address[1], page_address[0], address[4], address[3]]
    column_select = [column_address[1], column_address[0], address[2]]
    
    return row_select, column_select