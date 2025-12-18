"""
QUESTION:
Create a function named `check_prime(n)` that checks if a given integer `n` is a prime number and a program that takes user input for start, end, and increment values. The program should initialize a variable `counter` with the start value and increment it by the increment value until it exceeds the end value, checking if each value is prime and printing the result.
"""

def entrance(n, start, end, increment):
    def check_prime(num):
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True

    counter = start
    while counter <= end:
        if check_prime(counter):
            print(counter, 'is a prime number')
        else:
            print(counter)
        counter += increment