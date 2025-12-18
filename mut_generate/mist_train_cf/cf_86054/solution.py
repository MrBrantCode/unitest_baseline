"""
QUESTION:
Implement a function named `prime_digits_sum` that uses loops (while, for, nested loops) and control structures (break, continue, pass) to find all prime numbers in a given range, then for each prime number, calculate the sum of its digits. The function should print each prime number and its corresponding sum of digits. The range of numbers is from 1 to 100.
"""

def prime_digits_sum(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i += 6
        return True

    def sum_of_digits(n):
        sum = 0
        while(n > 0):
            digit = n % 10
            sum += digit
            n //= 10
        return sum

    for num in range(start, end + 1):
        if is_prime(num):
            print(f'{num} is a Prime Number')
            digit_sum = sum_of_digits(num)
            print(f'Sum of digits of {num} is {digit_sum}')