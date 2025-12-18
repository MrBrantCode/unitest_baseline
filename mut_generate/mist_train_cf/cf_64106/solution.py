"""
QUESTION:
Write a function `sum_of_squares` to calculate the sum of the series (n-1)^2 + (n-2)^2 + ... + 1^2 where n is a prime number. The function should check whether the input number is prime and return the sum if it is prime; otherwise, it should return an error message.
"""

def sum_of_squares(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if is_prime(n):
        total_sum = 0
        for i in range(1, n):
            total_sum += i**2
        return total_sum
    else:
        return "The number is not prime"