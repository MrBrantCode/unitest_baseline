"""
QUESTION:
Write a function named `calculate_physical_address` that takes two 16-bit integers (segment and offset) as parameters, representing the segment and offset registers in a 16-bit Intel 8086 processor. The function should return the 20-bit physical memory address calculated by shifting the segment left by 4 bits and adding the offset.
"""

def calculate_physical_address(segment, offset):
    return (segment << 4) + offset