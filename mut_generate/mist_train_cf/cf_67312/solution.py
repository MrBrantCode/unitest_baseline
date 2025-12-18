"""
QUESTION:
Write a function `prime_five_nine_twelve` that takes an integer `n` as input and returns the total count of prime numbers less than `n` that contain the digit 5 and have a digit sum divisible by 3. The function should not include `n` in the count.
"""

def prime_five_nine_twelve(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def digit_sum(num):
        return sum(int(digit) for digit in str(num))

    count = 0
    for i in range(2, n):
        if is_prime(i):
            if '5' in str(i) and digit_sum(i) % 3 == 0:
                count += 1
    return count