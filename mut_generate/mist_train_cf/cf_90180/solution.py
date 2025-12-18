"""
QUESTION:
Create a function called `countPrimeOccurrences` that takes two arguments: an array of integers and a target number. The function should count the number of occurrences of the target number in the array, but only if the target number is a prime number and the occurrence is greater than or equal to zero. The function should have a time complexity of O(n), where n is the length of the array.
"""

def countPrimeOccurrences(arr, num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for i in arr:
        if i >= 0 and is_prime(i) and i == num:
            count += 1
    return count