"""
QUESTION:
Create a function called "print_multiplication_table" that takes two integer parameters "x" and "y". The function should print the multiplication table for the range of integers from "x" to "y", provided that both "x" and "y" are positive numbers and "x" is less than or equal to "y". If the range contains any prime numbers, print a warning message indicating the presence of prime numbers in the range.
"""

def print_multiplication_table(x, y):
    """
    Prints the multiplication table for the range of integers from x to y.
    If the range contains any prime numbers, prints a warning message.

    Args:
        x (int): The start of the range (inclusive).
        y (int): The end of the range (inclusive).

    Returns:
        None
    """
    if x <= 0 or y <= 0:
        print("Error: Both x and y should be positive numbers.")
        return
    
    if x > y:
        print("Error: x should be less than or equal to y.")
        return
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    
    has_prime = any(is_prime(num) for num in range(x, y+1))
    
    if has_prime:
        print("Warning: The range contains prime numbers.")
    
    for i in range(x, y+1):
        print(str(i) + ":", end=" ")
        for j in range(x, y+1):
            product = i * j
            print(str(product) + "\t", end=" ")
        print()