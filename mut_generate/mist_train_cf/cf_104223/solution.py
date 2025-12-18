"""
QUESTION:
Write a function `prime_greater_than_10` that takes a list of positive integers as input. Return a list of integers that are both prime and greater than 10, and print the total count of such numbers.
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