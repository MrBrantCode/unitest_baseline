"""
QUESTION:
Given an array of matchstick lengths, write a function `makesquare(nums)` to determine if it's possible to construct a perfect square using all the matchsticks without breaking any. The total length of the matchsticks is within the range of 0 to 10^9, and the array of matchstick lengths does not exceed 15 in length. The function should return a boolean value indicating whether a square can be formed using all the matchsticks.
"""

def makesquare(nums):
    if not nums: return False
    total_length = sum(nums)
    if total_length % 4: return False
    nums.sort(reverse=True)
    side_length = total_length // 4
    sides = [0] * 4
    
    def dfs(index):
        if index == len(nums): return all(side == side_length for side in sides)
        for i, side in enumerate(sides):
            if side + nums[index] <= side_length:
                sides[i] += nums[index]
                if dfs(index + 1): return True
                sides[i] -= nums[index]
            if not side: break
        return False

    return dfs(0)