"""
QUESTION:
Write a function `print_fibonacci_sequence()` that takes no parameters and prints out the Fibonacci sequence up to the nth term. The function should first prompt the user to input the number of terms `n`, which must be within the range of 1 to 100 (inclusive). If `n` is outside this range, print "Please enter a number between 1 and 100." and terminate. If `n` is a prime number, print "Please enter a non-prime number." and terminate. The Fibonacci sequence should be generated and printed only when `n` meets the specified conditions.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_fibonacci_sequence():
    n = int(input("Enter the number of terms: "))
    if n < 1 or n > 100:
        print("Please enter a number between 1 and 100.")
        return
    
    if is_prime(n):
        print("Please enter a non-prime number.")
        return
    
    sequence = fibonacci_sequence(n)
    print("Fibonacci sequence:")
    for num in sequence:
        print(num)