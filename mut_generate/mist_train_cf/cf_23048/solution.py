"""
QUESTION:
Implement a function `findSmallestDivisible(arr)` that takes an array of at least two positive integers as input and returns the smallest positive integer that is divisible by all the numbers in the array. The solution should not use any built-in LCM function or additional data structures. The time complexity should be O(n), where n is the number of elements in the array, and the space complexity should be O(1).
"""

def findSmallestDivisible(arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = arr[0]
    for num in arr[1:]:
        lcm = (lcm * num) // gcd(lcm, num)
    return lcm