"""
QUESTION:
Create a function `print_pascal(n)` that generates a Pascal's Triangle of size `n`, color-codes each number based on whether it is a prime number (blue), a perfect square (green), or none of these (red), and handles invalid inputs (non-positive integers).
"""

def print_pascal(n):
    # Function to print color
    def print_color(num):
        if check_prime(num):
            return "\033[94m {}\033[00m".format(num)
        elif check_square(num):
            return "\033[92m {}\033[00m".format(num)
        else:
            return "\033[91m {}\033[00m".format(num)

    # Function to check prime
    def check_prime(num):
        if num <= 1:
            return False
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

    # Function to check perfect square
    def check_square(num):
        if num < 0:
            return False
        else:
            root = int(num**(0.5))
            return num == root*root

    # For printing pascal pattern
    arr = [[0]*n for _ in range(n)]
    for line in range(0, n):
        for i in range(0, line + 1):
            if i is 0 or i is line:
                arr[line][i] = 1
            else:
                arr[line][i] = (arr[line - 1][i - 1] +
                                arr[line - 1][i])
        for j in range(line + 1):
            print(print_color(arr[line][j]), end=" ")
        print("\n")