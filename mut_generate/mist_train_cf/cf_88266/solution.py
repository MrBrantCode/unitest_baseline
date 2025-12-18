"""
QUESTION:
Write a function named `find_prime_numbers` that takes two parameters `start` and `end` and returns a string of comma-separated numbers from `start` to `end` (inclusive) that are not divisible by both 2 and 3. The function should only accept positive integers greater than zero as inputs. The output string should be in ascending order.
"""

def find_prime_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int) or start <= 0 or end <= 0:
        return "Inputs must be positive integers greater than zero."
    
    prime_numbers = [num for num in range(start, end + 1) if num % 2 != 0 and num % 3 != 0]
    prime_numbers.sort()
    return ', '.join(map(str, prime_numbers))