"""
QUESTION:
Write a function called `generate_permutations` that takes an integer `n` as input and returns a list of all possible permutations of the numbers from 1 to `n`, along with the total count of permutations. The input integer `n` will be in the range 1 to 8. Do not use any built-in functions or libraries that directly generate permutations.
"""

def generate_permutations(n):
    def backtrack(nums, path, res):
        if len(path) == n:
            res.append(path[:])
            return
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(nums, path, res)
                path.pop()
    
    nums = [i for i in range(1, n+1)]
    res = []
    backtrack(nums, [], res)
    return res, len(res)