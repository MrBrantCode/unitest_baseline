"""
QUESTION:
Write a function named `find_avg_prime_numbers` that takes an integer `n` as input and prints the first `n` even numbers that are multiples of 4 and greater than 100, and where the sum of their digits is a prime number. The function should return the average of the prime numbers found. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_avg_prime_numbers(n):
    count = 0  # count of prime numbers found
    prime_sum = 0  # sum of prime numbers found

    def is_prime(num):
        if num <= 1:
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

    num = 104  # Starting number greater than 100 and a multiple of 4
    while count < n:
        digits_sum = sum(map(int, str(num)))  # sum of digits in the number

        # Check if the sum of digits is a prime number
        if is_prime(digits_sum):
            count += 1
            prime_sum += digits_sum

            print(num)

        num += 4  # Increment by 4 to get the next even number

    average = prime_sum / count if count > 0 else 0
    return average