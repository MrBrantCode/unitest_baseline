"""
QUESTION:
Write a function `print_zero_pattern(n)` that prints a zero (or cross) pattern using asterisks (*) and underscores (_) for a given integer `n`, where each row has exactly three characters and a prime number of asterisks and underscores, with a minimum of one asterisk and one underscore in each row. The function should not take any other parameters besides `n`.
"""

def print_zero_pattern(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(n):
        if is_prime(i+1):
            if (i+1) % 2 == 0:
                print('_**')
            else:
                print('*_*')
        else:
            print('_**')