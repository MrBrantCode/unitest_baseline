"""
QUESTION:
Given a list of positive integers of length between 1 and 10 (inclusive) and values between 2 and 1000 (inclusive), write a function `optimalDivision` that returns a string representing the optimal division operation with the maximum result by inserting any number of parentheses at any position to alter the precedence of operations. The function should take the list of integers as input and return a string devoid of any superfluous parentheses.
"""

def optimalDivision(nums):
    if len(nums) == 1:
        return str(nums[0])
    if len(nums) == 2:
        return str(nums[0]) + "/" + str(nums[1])
    res = str(nums[0]) + "/(" + str(nums[1])
    for num in nums[2:]:
        res += "/" + str(num)
    res += ")"
    
    return res