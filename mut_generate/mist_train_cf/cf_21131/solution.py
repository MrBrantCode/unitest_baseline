"""
QUESTION:
Write a function named `get_valid_input` that takes no arguments and returns a positive integer. The input should be a positive integer greater than 10 and less than or equal to 100, and it must be a prime number. If the input does not meet these conditions, the function should continue to prompt the user for input until a valid integer is provided. Use a recursive helper function `is_prime(n, i=2)` to check if the input is a prime number.
"""

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i+1)

def get_valid_input():
    while True:
        try:
            num = int(input("Enter a positive integer greater than 10 and less than or equal to 100: "))
            if num > 10 and num <= 100:
                if is_prime(num):
                    return num
                else:
                    print("Input is not a prime number.")
            else:
                print("Input is not within the specified range.")
        except ValueError:
            print("Input is not a valid integer.")