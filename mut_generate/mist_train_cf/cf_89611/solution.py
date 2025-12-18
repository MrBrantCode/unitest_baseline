"""
QUESTION:
Write a function `find_missing_numbers(nums)` that finds the missing number(s) in an array of n consecutive integers, where the array may contain duplicate numbers. The function should return the missing number(s) in ascending order without using any built-in functions, libraries, or extra data structures. The time complexity should be O(n), where n is the length of the input array.
"""

def find_missing_numbers(nums):
    missing = []  
    expected = 1  
    
    for num in nums:
        if num < expected:
            continue
        elif num == expected:
            expected += 1
        elif num > expected:
            for i in range(expected, num):
                missing.append(i)
            expected = num + 1
    
    return missing