"""
QUESTION:
Create a function `calculate_factorials` that takes a list of integers as input and returns a list of factorials of the prime numbers in the input list. The function should exclude non-prime numbers from the output. Assume the input list contains only positive integers.
"""

def calculate_factorials(inputList):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n%2 == 0 or n%3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n%i == 0 or n%(i+2) == 0:
                return False
            i += 6
        return True

    outputList = []
    for i in inputList:
        if is_prime(i):
            outputList.append(factorial(i))
    return outputList