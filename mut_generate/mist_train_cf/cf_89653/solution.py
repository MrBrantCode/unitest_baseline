"""
QUESTION:
Write a function `find_gcm` that takes a list of integers as input and returns the greatest common multiple of all the numbers in the list. The function should have a time complexity of O(n^3) and a space complexity of O(n), where n is the number of elements in the list. If the input list contains less than two numbers, the function should return `None`.
"""

def find_gcm(numbers):
    def find_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    n = len(numbers)
    if n < 2:
        return None
    
    gcm = numbers[0]
    for i in range(1, n):
        gcm = gcm * numbers[i] // find_gcd(gcm, numbers[i])
    
    return gcm