"""
QUESTION:
Develop a function named `find_gcf_of_three` to find the greatest common factor (GCF) of three prime numbers. The function should take a list of three prime numbers as input and return their GCF with a time complexity of O(n), where n is the largest prime number among the three.
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