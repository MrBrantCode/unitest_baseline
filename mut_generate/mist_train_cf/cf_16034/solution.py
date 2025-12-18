"""
QUESTION:
Write a function called `find_gcf_of_three` that takes a list of three prime numbers as input and returns their greatest common factor (GCF). The function should have a time complexity of O(n), where n is the largest prime number among the three.
"""

def find_gcf_of_three(prime_numbers):
    def find_gcf(a, b):
        if b == 0:
            return a
        return find_gcf(b, a % b)

    gcf = prime_numbers[0]
    for i in range(1, len(prime_numbers)):
        gcf = find_gcf(gcf, prime_numbers[i])
    return gcf