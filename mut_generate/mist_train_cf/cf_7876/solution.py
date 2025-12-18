"""
QUESTION:
Generate a function `generate_numbers(N)` that produces a sequence of the first N numbers that are greater than or equal to 100 and less than or equal to 1000. The sequence should only include numbers that are divisible by both 5 and 7, and the numbers should be in increasing order.
"""

def generate_numbers(N):
    """Generate a sequence of the first N numbers that are greater than or equal to 100 and less than or equal to 1000.
    The sequence should only include numbers that are divisible by both 5 and 7, and the numbers should be in increasing order."""
    
    count = 0
    num = 100
    result = []
    
    while count < N:
        if 100 <= num <= 1000 and num % 35 == 0:
            result.append(num)
            count += 1
        num += 1
        
    return result