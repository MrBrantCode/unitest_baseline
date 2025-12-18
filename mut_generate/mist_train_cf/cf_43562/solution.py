"""
QUESTION:
Write a function `judgePoint24(nums)` that takes a list of four distinct numbers between 1 and 9 as input and returns `True` if it's possible to get exactly 24 using basic arithmetic operations (+, -, *, /) and parentheses, and `False` otherwise. The division operation should be real division, not integer division, and the numbers cannot be concatenated or used as unary operators.
"""

def judgePoint24(nums):
    if not nums:
        return False
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                newNums = [nums[k] for k in range(len(nums)) if i != k and j != k]
                if nums[i] > nums[j]: 
                    newNums.append(nums[i]-nums[j])
                    if judgePoint24(newNums):
                        return True
                    newNums.pop()
                newNums.append(nums[i]*nums[j])
                if judgePoint24(newNums):
                    return True
                newNums.pop()
                if nums[j] != 0:
                    newNums.append(nums[i]/nums[j])
                    if judgePoint24(newNums):
                        return True
                    newNums.pop()
                if nums[i] != 0:
                    newNums.append(nums[j]/nums[i])
                    if judgePoint24(newNums):
                        return True
                    newNums.pop()
                newNums.append(nums[i]+nums[j])
                if judgePoint24(newNums):
                    return True
                newNums.pop()
    return False