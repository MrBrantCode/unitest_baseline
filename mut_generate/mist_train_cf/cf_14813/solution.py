"""
QUESTION:
Create a function called fibonacci_sequence that takes a parameter length and returns a Fibonacci sequence of the specified length. The function should return an empty sequence if the length is less than or equal to 0, a sequence with only 0 if the length is 1, and a sequence with 0 and 1 if the length is 2. For lengths greater than 2, the function should generate the Fibonacci sequence up to the specified length.
"""

def fibonacci_sequence(length):
    """
    Returns a Fibonacci sequence of the specified length.

    Args:
        length (int): The length of the Fibonacci sequence to generate.

    Returns:
        list: A list of Fibonacci numbers up to the specified length.
    """
    if length <= 0:
        return []
    elif length == 1:
        return [0]
    elif length == 2:
        return [0, 1]
    
    sequence = [0, 1]
    num1, num2 = 0, 1
    
    while len(sequence) < length:
        next_num = num1 + num2
        sequence.append(next_num)
        num1, num2 = num2, next_num
    
    return sequence