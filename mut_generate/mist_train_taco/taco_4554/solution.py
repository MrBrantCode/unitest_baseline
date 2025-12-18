"""
QUESTION:
For "x", determine how many positive integers less than or equal to "x" are odd but not prime. Assume "x" is an integer between 1 and 10000.

Example: 5 has three odd numbers (1,3,5) and only the number 1 is not prime, so the answer is 1

Example: 10 has five odd numbers (1,3,5,7,9) and only 1 and 9 are not prime, so the answer is 2
"""

def count_odd_non_prime(x: int) -> int:
    def not_prime(num: int) -> bool:
        if num == 1:
            return True
        for y in range(2, int(num ** 0.5) + 1):
            if num % y == 0:
                return True
        return False
    
    return sum((not_prime(num) for num in range(1, x + 1, 2)))