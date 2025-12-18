"""
QUESTION:
Write a function `fibonacci_prime` that takes an integer `n` as input and returns two lists: one containing the Fibonacci sequence up to `n` and another containing the prime numbers in the derived Fibonacci sequence. The function should have a time complexity of O(n).
"""

def fibonacci_prime(n):
    """Function to generate fibonacci sequence upto n and find prime numbers"""
    
    def check_prime(number):
        """Nested function to check if a number is prime"""
        if number == 0 or number == 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
    fibonacci = [0, 1]
    prime = []
    
    # Generate fibonacci sequence upto n
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    # Find prime numbers
    for num in fibonacci:
        if check_prime(num):
            prime.append(num)
    
    return fibonacci, prime