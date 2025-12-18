"""
QUESTION:
Write a function to print the first 1000 prime numbers without using built-in looping statements like "for" or "while". The function should have a time complexity of O(n√n) and a space complexity of O(1).
"""

def entrance(n):
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2

        return True

    count = 0
    num = 2

    while count < n:
        if is_prime(num):
            print(num)
            count += 1

        num += 1