"""
QUESTION:
Create a function `prime_numbers(n)` that generates a list of prime numbers between 2 and `n` (inclusive). The function should return a list of integers. The input `n` is an integer greater than or equal to 2.
"""

def prime_numbers(n):
    prime_nums = []
    for num in range(2, n + 1):
        if num > 1:
            for i in range(2, num): 
                if (num % i) == 0: 
                    break
            else:
                prime_nums.append(num)
    return prime_nums