"""
QUESTION:
Write a function named `compute_and_factorize` that takes a list of numbers as input. The function should return a dictionary where the keys are the input numbers and the values are another dictionary containing the cube, square, factors, and whether the number is prime.
"""

def compute_and_factorize(numbers):
    results = {}
    for num in numbers:
        # compute square and cube
        cube = num ** 3
        square = num ** 2

        # compute factors
        factors = [i for i in range(1, num+1) if num % i == 0]
        
        # check if number is prime
        is_prime = len(factors) == 2

        # populate results
        results[num] = {
            "cube": cube,
            "square": square,
            "factors": factors,
            "is_prime": is_prime
        }
    return results