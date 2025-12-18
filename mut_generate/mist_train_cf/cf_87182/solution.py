"""
QUESTION:
Create a function called "print_perfect_numbers" that takes in an integer parameter "n" and prints all perfect numbers between 0 to n, along with their prime factors. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. Prime factors are the prime numbers that can evenly divide a number without leaving a remainder. The function should return the list of perfect numbers and a dictionary where each key is a perfect number and its corresponding value is another dictionary containing the prime factors of the perfect number and their counts. The function should only consider numbers from 1 to n (inclusive).
"""

def print_perfect_numbers(n):
    perfect_numbers = []
    prime_factors = {}

    for num in range(1, n + 1):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        
        sum_divisors = sum(divisors)
        if num == sum_divisors:
            perfect_numbers.append(num)
            
            for divisor in divisors:
                if divisor < 2:
                    continue
                is_prime = True
                for i in range(2, int(divisor ** 0.5) + 1):
                    if divisor % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    if num not in prime_factors:
                        prime_factors[num] = {}
                    if divisor not in prime_factors[num]:
                        prime_factors[num][divisor] = 1
                    else:
                        prime_factors[num][divisor] += 1

    print("Perfect numbers:", perfect_numbers)
    print("Prime factors:", prime_factors)
    return perfect_numbers, prime_factors