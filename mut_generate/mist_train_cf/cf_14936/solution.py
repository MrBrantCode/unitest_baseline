"""
QUESTION:
Find the least common multiple (LCM) of an array of numbers using the given formula: LCM(a, b) = (a * b) / GCD(a, b), where GCD is calculated using the Euclidean algorithm. The function should take an array of numbers as input, with at least two numbers, and all numbers being positive integers. Implement this function without using the built-in LCM function.
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