"""
QUESTION:
Write a function named `print_pattern` that takes an integer `n` as input and prints a pattern of `n` rows and `n` columns, where each element is a unique number starting from 1 and incrementing by 1 for each element moving to the right. The function should first check if `n` is a prime number and print "Invalid input. Please enter a prime number." if it is not. If `n` is prime, the function should print the pattern with each row on a new line and elements separated by spaces.
"""

def print_pattern(n):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not is_prime(n):
        print("Invalid input. Please enter a prime number.")
        return

    pattern = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            pattern[i][j] = num
            num += 1

    for row in pattern:
        print(' '.join(map(str, row)))