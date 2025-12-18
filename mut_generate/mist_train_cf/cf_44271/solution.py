"""
QUESTION:
Write a function named `get_prime_numbers` that takes a range of integers and returns a list of prime numbers within that range. The function should use a for-loop algorithm and consider a number as prime if it has exactly two positive integer factors, 1 and itself. The input range will be inclusive of the start value but exclusive of the end value. The output list should be in ascending order.
"""

def get_prime_numbers(start, end):
    """
    Returns a list of prime numbers within the given range.
    
    Args:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (exclusive).
    
    Returns:
    list: A list of prime numbers in the range.
    """
    prime_nums = []
    for num in range(start, end):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return prime_nums