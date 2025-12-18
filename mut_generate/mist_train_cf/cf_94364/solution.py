"""
QUESTION:
Create a function named `generate_fibonacci` that generates a series of Fibonacci numbers up to a certain number of items `n` and calculates the sum of all the prime Fibonacci numbers in the series. The function should take an integer `n` as input and return a tuple containing the Fibonacci series and the sum of the prime Fibonacci numbers.
"""

def generate_fibonacci(n):
    def is_prime(num):
        if num < 2:  
            return False
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  
                return False
        
        return True

    fibonacci_series = [0, 1]  
    prime_sum = 0  
    
    while len(fibonacci_series) < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]  
        fibonacci_series.append(next_number)  
        
        if is_prime(next_number):  
            prime_sum += next_number  
    
    return fibonacci_series, prime_sum