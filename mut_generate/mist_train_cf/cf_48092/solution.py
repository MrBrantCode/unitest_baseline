"""
QUESTION:
Develop a function named find_prime_numbers that takes a list of integers as input and returns a tuple. The first element of the tuple should be a sorted list of prime numbers from the input list in ascending order. The second element of the tuple should be the product of all prime numbers in the list. The function should ignore non-integer, non-positive numbers, and zero. It should also be able to handle the case where the product of prime numbers exceeds the maximum limit for integers in Python.
"""

def find_prime_numbers(input_list):
    prime_numbers = []
    multiplication_of_primes = 1
    for num in input_list:
        if not isinstance(num, int):
            continue
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
                multiplication_of_primes *= num
    return (sorted(prime_numbers), multiplication_of_primes)