"""
QUESTION:
Write a function named `range_prime` that takes two integers C and D as input and prints all prime numbers in the range [C, D] using recursive techniques. The function should handle the case where C is greater than D.
"""

def range_prime(C, D):
    """Recursively checks a range of numbers for primes"""
    
    def check_prime(num, div = None):
        """Recursively checks if a number is prime"""
        
        if num < 2:
            return False
        elif num == 2 : 
            return True
        elif div is None:
            div = num - 1

        while div >= 2:
            if num % div == 0:
                return False
            else:
                div -= 1
        else:
            return True

    if C > D:
        return
    if check_prime(C):
        print(C)
    return range_prime(C + 1, D)