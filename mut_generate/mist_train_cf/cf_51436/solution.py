"""
QUESTION:
Create a function named `PrimeFibonacci` that generates Fibonacci numbers up to a specified limit and returns only the prime numbers from the generated sequence. The function should be able to handle any positive integer limit.
"""

def PrimeFibonacci(limit):
    def check_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    numbers = [0, 1]
    while numbers[-1] + numbers[-2] < limit:
        numbers.append(numbers[-1] + numbers[-2])
    return [num for num in numbers if check_prime(num)]