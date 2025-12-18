"""
QUESTION:
Create a function named `print_prime_multiplication_table` that takes a single integer `n` as an argument and prints out the corresponding multiplication table, but only displays the products where both the row and column numbers are prime. The function should handle cases where `n` is not a positive integer by displaying an error message.
"""

def print_prime_multiplication_table(n):
    # Check if the input is a positive integer
    if not isinstance(n, int) or n <= 0:
        print("Error: Input must be a positive integer.")
        return
    
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Print the prime multiplication table
    for i in range(1, n+1):
        row = ""
        for j in range(1, n+1):
            if is_prime(i) and is_prime(j):
                row += str(i*j) + "\t"
        if row:
            print(row)