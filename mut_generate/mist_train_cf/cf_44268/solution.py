"""
QUESTION:
Implement a function `calculatePhysicalAddress` that simulates the working of segment and offset registers in a 16-bit Intel 8086 processor. The function should take a 16-bit segment register value and a 16-bit offset register value as input and return the calculated 20-bit physical address. The physical address should be calculated as (segment * 16) + offset. If the offset value exceeds 0xFFFF, consider it as wrapping around. Assume that the segment and offset register values are always non-negative integers. The function should not handle memory relocation.
"""

def calculatePhysicalAddress(segment, offset):
    """
    Simulates the working of segment and offset registers in a 16-bit Intel 8086 processor.
    
    Parameters:
    segment (int): 16-bit segment register value
    offset (int): 16-bit offset register value
    
    Returns:
    int: Calculated 20-bit physical address
    """
    return (segment << 4) + (offset % 0x10000)