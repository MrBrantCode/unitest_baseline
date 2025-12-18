"""
QUESTION:
Write a function `find_perfect_numbers(N)` that prints all perfect numbers between 1 and a given number N (inclusive). A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding the number itself. The function should take an integer N as a parameter and print all perfect numbers in the specified range.
"""

def find_perfect_numbers(N):
    def is_perfect_number(num):
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num / i) == num:
                    sum = sum + i + num/i
                else:
                    sum = sum + i
                i += 1
        return sum == num and num!=1

    for i in range(1, N+1):
        if is_perfect_number(i):
            print(i)