"""
QUESTION:
Create a function called `print_multiplication_table` that takes two integer parameters `x` and `y`. The function should print the multiplication table for the range of integers from `x` to `y`. The function must check if both `x` and `y` are positive numbers and if `x` is less than or equal to `y`. If either condition is not met, it should print an error message and return. Additionally, the function should check if the range contains prime numbers and print a warning message if it does. The function should then print the multiplication table with the row numbers followed by their products with all numbers in the range, separated by tabs.
"""

def print_multiplication_table(x, y):
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
    
    prime_numbers = [num for num in range(x, y+1) if is_prime(num)]
    
    if prime_numbers:
        print("Warning: The range contains prime numbers.")
    
    for i in range(x, y+1):
        print(str(i) + ":", end=" ")
        for j in range(x, y+1):
            product = i * j
            print(str(product) + "\t", end=" ")
        print()