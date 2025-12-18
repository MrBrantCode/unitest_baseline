"""
QUESTION:
Write a function called `prime_greater_than_10` that takes a list of positive integers as input and returns a new list containing only the prime numbers greater than 10. The function should also print the total count of numbers that meet these criteria.
"""

def prime_greater_than_10(numbers):
    prime_numbers = []
    count = 0
    
    for number in numbers:
        if number > 10:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(number)
                count += 1
    
    print("Total count:", count)
    return prime_numbers