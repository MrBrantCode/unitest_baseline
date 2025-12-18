"""
QUESTION:
Create a function `generate_sequence(start, ratio, length)` that generates a unique geometric sequence of a specified length. The sequence must start with the given number, be multiplied by the given ratio, and be at least 10 elements long. The sequence cannot include any negative numbers or fractions.
"""

def generate_sequence(start, ratio, length):
    """
    Generate a unique geometric sequence of a specified length.
    
    Args:
    start (int): The starting number of the sequence.
    ratio (int): The ratio to multiply each number in the sequence by.
    length (int): The length of the sequence.
    
    Returns:
    list: A list of integers representing the geometric sequence.
    """
    sequence = []
    num = start
    for _ in range(length):
        sequence.append(num)
        num *= ratio
    return sequence