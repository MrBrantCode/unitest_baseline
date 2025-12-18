"""
QUESTION:
Implement the function `allocate_memory_and_string(count: int, string_constant: str) -> int` where:
- `count` (1 <= count <= 100) is an integer representing the number of data words to allocate.
- `string_constant` is a non-empty ASCII string constant that needs to be placed in memory.

The function should allocate memory for the data words, place the ASCIIZ string constant in memory, and return the address of the string constant, starting from the initial memory address 0x123450.
"""

def allocate_memory_and_string(count: int, string_constant: str) -> int:
    memory_addr = 0x123450  # Initial memory address
    data_words = []
    
    for _ in range(count):
        data_words.append(memory_addr)
        memory_addr += 2
    
    string_addr = memory_addr  # Address for the ASCIIZ string constant
    
    return string_addr