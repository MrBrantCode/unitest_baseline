"""
QUESTION:
Write a function `find_lcm` that takes an array of at least two positive integers as input and returns their least common multiple (LCM) using the Euclidean algorithm for GCD calculation. The LCM should be calculated efficiently without using the built-in LCM function.
"""

def find_lcm(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = nums[0]
    for i in range(1, len(nums)):
        lcm = (lcm * nums[i]) // gcd(lcm, nums[i])
    return lcm