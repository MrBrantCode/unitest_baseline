"""
QUESTION:
Write a function `starts_one_ends` that takes a positive integer `n` as input and returns the count of `n`-digit positive integer values that originate or terminate with the digit 1 and are either prime or Fibonacci numbers.
"""

def starts_one_ends(n):
    def is_prime(num):
        if num <= 1 or (num % 2 == 0 and num > 2): 
            return False
        return all(num % i for i in range(3, int(num**0.5) + 1, 2))

    def is_fibonacci(num):
        x = 0
        y = 1
        while y < num:
            z = x + y
            x = y
            y = z
        return y == num

    start = 10 ** (n - 1) + 1
    end = 10 ** n 
    step = 10 if n == 1 else 100
    numbers = list(range(start, end, step))
    numbers.extend(list(range(start - 1, end - 1, step)))
    count = 0
    for num in numbers:
        if is_prime(num) or is_fibonacci(num):
            count += 1
    return count