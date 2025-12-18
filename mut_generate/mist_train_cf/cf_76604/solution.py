"""
QUESTION:
Write a function named `check_deficiency_abundance` that takes a list of integers as input and classifies each number as 'abundant' (or 'excessive'), 'deficient', or 'perfect' based on the sum of its proper divisors. A number is considered abundant if the sum of its proper divisors is greater than the number itself, deficient if the sum is less than the number, and perfect if the sum equals the number. The function should print out the classification for each number in the input list.
"""

def check_deficiency_abundance(numbers):
    def find_divisors(n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i:
                continue
            if i == n // i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
        return divisors

    for number in numbers:
        divisors = find_divisors(number)
        sum_divisors = sum(divisors)

        if sum_divisors < number:
            print(f"{number} is a deficient number.")
        elif sum_divisors > number:
            print(f"{number} is an abundant number.")
        else:
            print(f"{number} is a perfect number.")