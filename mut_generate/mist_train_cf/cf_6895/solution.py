"""
QUESTION:
Design an algorithm to find the greatest common multiple (GCM) of all numbers in a list. The function should be named `find_gcm` and take a list of numbers as input. The algorithm must meet the time complexity requirement of O(n^3) and the space complexity requirement of O(n).
"""

def find_gcm(numbers):
    n = len(numbers)
    if n < 2:
        return None
    
    def find_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcm = numbers[0]
    for i in range(1, n):
        gcm = gcm * numbers[i] // find_gcd(gcm, numbers[i])
    
    return gcm