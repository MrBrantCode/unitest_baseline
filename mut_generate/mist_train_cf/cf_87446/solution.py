"""
QUESTION:
Create a function `get_descending_primes` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list, sorted in descending order. The time complexity of the function should be O(n), where n is the length of the original list.
"""

def get_descending_primes(originalList):
    primes = []
    for num in originalList:
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)