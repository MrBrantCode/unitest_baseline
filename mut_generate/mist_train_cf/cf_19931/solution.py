"""
QUESTION:
Write a function `add_prime_palindrome` that takes a list of prime numbers as input and appends a new prime number to the list. The new prime number must be a palindrome and greater than the last prime number in the list. The function should not take any other parameters.
"""

def add_prime_palindrome(prime_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    i = prime_list[-1] + 1
    while True:
        if is_prime(i) and is_palindrome(i):
            prime_list.append(i)
            break
        i += 1