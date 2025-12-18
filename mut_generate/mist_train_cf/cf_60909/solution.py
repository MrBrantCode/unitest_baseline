"""
QUESTION:
Create a function called `classify_number` that takes an integer `x` as input and classifies it as one or more of the following: positive integer, negative integer, zero, even number, odd number, prime number, or a number in the Fibonacci series. The function should accurately classify the integer under multiple conditions if applicable.
"""

def classify_number(x):
    # Helper function to check if number is prime
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    # Helper function to check if number is Fibonacci number
    def is_fibonacci(n):
        i = 0
        j = 1
        while j < n:
            k = i + j
            i = j
            j = k
        return n == j

    if isinstance(x, int): 
        if x > 0:
            print(str(x) + " is a positive integer.")
        elif x < 0:
            print(str(x) + " is a negative integer.")
        else:
            print(str(x) + " is zero.")
            
        if x % 2 == 0:
            print(str(x) + " is an even number.")
        else:
            print(str(x) + " is an odd number.")
            
        if is_prime(x):
            print(str(x) + " is a prime number.")
            
        if is_fibonacci(x):
            print(str(x) + " is a number in Fibonacci series.")
    else:
        print("Input is not an integer.")