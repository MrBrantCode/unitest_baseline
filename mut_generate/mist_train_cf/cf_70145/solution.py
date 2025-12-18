"""
QUESTION:
You are given an array of integers representing the lengths of matchsticks. Determine if it's possible to construct a perfect square using all the matchsticks without breaking any. If it's not possible, return the minimum number of matchsticks that need to be removed to form a square. The total length of the matchsticks is within the range of 0 to 10^9 and the array of matchstick lengths does not exceed 15 in length. Implement a function `makesquare` that takes the array of matchstick lengths as input and returns a boolean value if a square can be formed or the minimum number of matchsticks to be removed if a square cannot be formed.
"""

def makesquare(nums):
    n = len(nums)
    nums.sort(reverse=True)
    tot = sum(nums)
    edge = tot // 4
    if n < 4 or tot % 4 != 0 or nums[0] > edge:  
        return max(0, edge * 4 - tot)  

    def dfs(index, side, cnt):
        if cnt == 3:  
            return True
        if side == edge:  
            return dfs(0, 0, cnt+1)
        for i in range(index, len(nums)):
            if nums[i] + side > edge:  
                continue
            if dfs(i+1, nums[i]+side, cnt):  
                return True
            nums[i], nums[-1] = nums[-1], nums[i]  
            if nums[i] == 0 or side == 0:  
                break
            nums[i], nums[-1] = nums[-1], nums[i]  
        return False

    return 0 if dfs(0, 0, 0) else max(0, edge * 4 - tot)