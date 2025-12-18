"""
QUESTION:
Write a recursive function `product(num)` that calculates the product of all prime numbers less than or equal to `num` that are also Fibonacci numbers and not divisible by 3. The function should return the product of these numbers.
"""

def product(num):
    """ calculating the product of fibonacci prime numbers not divisible by three """
    def is_prime(n):
        """ checking if a number is prime """
        if n < 2: return False
        if n == 2 or n == 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0: return False
            i += 6
        return True

    def is_fibonacci(n):
        """ checking if a number is fibonacci """
        x = 0
        y = 1
        while y < n:
            z = x + y
            x = y
            y = z
        return y == n

    def not_divisible_by_3(n):
        """ checking if a number is not divisible by 3 """
        return n % 3 != 0

    if num <= 0:
        return 1
    elif not_divisible_by_3(num) and is_prime(num) and is_fibonacci(num):
        return num * product(num-1)
    else:
        return product(num-1)