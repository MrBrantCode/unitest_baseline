"""
QUESTION:
Write a function `is_prime(num)` that takes a positive integer `num` less than or equal to 10^6 and returns two values: a boolean indicating whether `num` is prime and the smallest prime number larger than `num`.
"""

def entrance(num):
    def is_divisible(num, divisor):
        return num % divisor == 0
    
    def find_next_prime(num):
        while True:
            num += 1
            if is_prime(num):
                return num
    
    def is_prime(num):
        if num < 2:
            return False
        
        for divisor in range(2, int(num ** 0.5) + 1):
            if is_divisible(num, divisor):
                return False
        
        return True
    
    prime = is_prime(num)
    next_prime = find_next_prime(num)
    
    return prime, next_prime