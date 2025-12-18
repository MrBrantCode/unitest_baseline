"""
QUESTION:
Your work is to write a method that takes a value and an index, and returns the value with the bit at given index flipped.

The bits are numbered from the least significant bit (index 1).

Example:
```python
flip_bit(15, 4) == 7 # 15 in binary is 1111, after flipping 4th bit, it becomes 0111, i.e. 7
flip_bit(15, 5) == 31 # 15 in binary is 1111, 5th bit is 0, after flipping, it becomes 11111, i.e., 31
```
Note : index number can be out of number's range : e.g number is 3 (it has 2 bits) and index number is 8(for C# this number is up to 31) -> result will be 131 

See more examples in test classes

Good luck!
"""

def flip_bit(value: int, bit_index: int) -> int:
    """
    Flips the bit at the specified index in the given value.

    Parameters:
    - value (int): The integer value whose bit needs to be flipped.
    - bit_index (int): The index of the bit to be flipped, starting from 1 (least significant bit).

    Returns:
    - int: The new value after flipping the specified bit.
    """
    return value ^ (1 << (bit_index - 1))