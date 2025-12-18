"""
QUESTION:
Create a function `print_positive_divisors(x)` that takes an integer `x` and prints all its positive divisors in ascending order, along with their sum. The function should handle invalid inputs: if `x` is less than 1, it should print "Invalid input" and terminate; if `x` is 1, it should print "1 has no positive divisors" and terminate.
"""

def print_positive_divisors(x):
    if x < 1:
        print("Invalid input")
        return
    elif x == 1:
        print("1 has no positive divisors")
        return

    divisors = [i for i in range(1, x + 1) if x % i == 0]
    print("Positive divisors:", divisors)
    print("Sum of divisors:", sum(divisors))