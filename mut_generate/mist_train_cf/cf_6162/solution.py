"""
QUESTION:
Create a function called `analyze_number` that takes an integer as input and prints the following: 

- "This is an even number" if the number is even, otherwise "This is an odd number".
- "This is a prime number" if the number is a prime number. If it's not prime, print "This is not a prime number" and all the factors of the number.
- "This is a perfect square" if the number is a perfect square.
- "This is a multiple of 5" if the number is a multiple of 5.

The function should only consider numbers between 1 and 1000 (inclusive).
"""

def analyze_number(n):
    """
    Analyze a number and print its properties.

    Args:
    n (int): The number to be analyzed.

    Returns:
    None
    """

    # Check if the number is within the specified range
    if not 1 <= n <= 1000:
        print("Number out of range. Please enter a number between 1 and 1000.")
        return

    # Check if the number is even or odd
    if n % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

    # Check if the number is prime
    is_prime = True
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")
        print("Factors:", end=" ")
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, end=" ")
        print()

    # Check if the number is a perfect square
    if n ** 0.5 == int(n ** 0.5):
        print("This is a perfect square")

    # Check if the number is a multiple of 5
    if n % 5 == 0:
        print("This is a multiple of 5")