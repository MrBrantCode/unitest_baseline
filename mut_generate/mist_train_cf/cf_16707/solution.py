"""
QUESTION:
Create a function named `generate_fibonacci` that takes an integer `n` as input and generates the first `n` numbers in the Fibonacci series. The function should also calculate the sum of all prime numbers in the generated series. The Fibonacci series should start with [0, 1].
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