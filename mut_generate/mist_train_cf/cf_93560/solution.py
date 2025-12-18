"""
QUESTION:
Create a function called `prime_difference` that takes a list of integers as input. The function should first sort the list in descending order. Then, it should find all prime numbers in the sorted list and store them in a separate list. Finally, the function should calculate and return the difference between the largest and smallest prime numbers in the list. If the list does not contain any prime numbers, the function should return a message "No prime numbers found."
"""

def prime_difference(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    numbers.sort(reverse=True)
    primes = [number for number in numbers if is_prime(number)]
    
    if not primes:
        return "No prime numbers found."
    else:
        return primes[0] - primes[-1]