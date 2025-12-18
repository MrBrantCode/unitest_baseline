"""
QUESTION:
Write a function `count_perfect_lucas_numbers(n)` that takes an integer `n` as input and returns the quantity of perfect numbers within the first `n` numbers of the Lucas series. A perfect number is a positive integer which is equal to the sum of its positive divisors excluding the number itself. A Lucas number is a sequence of numbers in which each number is the sum of the two preceding ones.
"""

def count_perfect_lucas_numbers(n):
    def is_perfect(num):
        total = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    total = total + i + num//i
                else:
                    total = total + i
                i += 1
        return total == num and num!=1

    a = 2
    b = 1
    count = 0
    for _ in range(n):
        if is_perfect(a):
            count += 1
        a, b = b, a + b
    return count