"""
QUESTION:
Convert integers to binary as simple as that. You would be given an integer as a argument and you have to return its binary form.
To get an idea about how to convert a decimal number into a binary number, visit here.

**Notes**: negative numbers should be handled as two's complement; assume all numbers are integers stored using 4 bytes (or 32 bits) in any language.

Your output should ignore leading 0s.

So, for example:
```python
to_binary(3)=="11"
to_binary(-3)=="11111111111111111111111111111101"
```

*Be Ready for Large Numbers. Happy Coding ^_^*
"""

def convert_to_binary(n: int) -> str:
    """
    Converts an integer to its binary representation, considering two's complement for negative numbers.

    Parameters:
    n (int): The integer to be converted.

    Returns:
    str: The binary representation of the integer, ignoring leading zeros.
    """
    # Mask to handle 32-bit two's complement representation
    mask = 4294967295  # Equivalent to 0xFFFFFFFF
    
    # Convert the number to its 32-bit binary representation
    binary_representation = '{:0b}'.format(n & mask)
    
    return binary_representation