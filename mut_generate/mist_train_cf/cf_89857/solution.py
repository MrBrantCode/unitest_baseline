"""
QUESTION:
Create a function called `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should consider the absolute value of each number when determining primality, allowing negative numbers to be included in the output if they are prime. The returned list must be sorted in descending order.
"""

def get_prime_numbers(numbers):
    prime_numbers = []
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for num in numbers:
        if is_prime(abs(num)):
            prime_numbers.append(num)
    
    prime_numbers.sort(reverse=True)
    return prime_numbers