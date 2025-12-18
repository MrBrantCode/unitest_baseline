"""
QUESTION:
Create a function called `print_pattern` that takes one argument `n`. The function should print a pattern consisting of n rows and n columns where each element in the pattern is a number. The pattern should start with 1 in the top-left corner and increment by 1 for each element moving to the right. When reaching the end of a row, the pattern should continue in the next row, but starting from the first column. The function should check if `n` is a prime number before printing the pattern and output "Invalid input. Please enter a prime number." if `n` is not a prime number.
"""

def print_pattern(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
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
        for num in row:
            print(num, end=" ")
        print()