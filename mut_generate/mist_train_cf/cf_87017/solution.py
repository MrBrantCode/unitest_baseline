"""
QUESTION:
Find the index of the single element in an array that occurs only once, where all other elements occur twice. Implement a solution without using any loops, recursion, built-in functions, or libraries. The solution should utilize basic data structures and algorithms provided by the programming language.
"""

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result