"""
QUESTION:
Create a function named `fizz_buzz_primes` that prints the FizzBuzz series where each term must be a prime number, up to the 1000th term.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def fizz_buzz_primes():
    count = 0
    num = 1
    while count < 1000:
        if is_prime(num):
            count += 1
            if count % 3 == 0 and count % 5 == 0:
                print("FizzBuzz")
            elif count % 3 == 0:
                print("Fizz")
            elif count % 5 == 0:
                print("Buzz")
            else:
                print(count)
        num += 1