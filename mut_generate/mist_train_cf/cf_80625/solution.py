"""
QUESTION:
Create a function named `fibonacci_and_prime` that generates a Fibonacci sequence up to a given number `y` and identifies whether each number in the sequence is a prime number or not. The function should return or print the Fibonacci sequence along with the primality of each number. The input `y` is a positive integer and the function should be able to handle it. Note that the function should be able to handle large inputs but does not necessarily need to be optimized for it.
"""

def fibonacci_and_prime(y):
    def generate_fibonacci(num):
        fib_sequence = [0, 1]
        while True:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            if next_number > num:
                break
            fib_sequence.append(next_number)
        return fib_sequence

    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib_sequence = generate_fibonacci(y)
    for number in fib_sequence:
        if check_prime(number):
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')