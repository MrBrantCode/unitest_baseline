"""
QUESTION:
Design a function named `permutations` that takes a list of numbers as input and prints all the unique permutations of the list, then returns the total number of permutations. The function should not take any duplicate numbers in the permutations into account.
"""

def permutations(nums):
    def backtrack(nums, perm, res):
        if len(perm) == len(nums):
            res.append(perm[:])  # Make a copy of the current permutation
        else:
            for num in nums:
                if num not in perm:
                    perm.append(num)  # Choose
                    backtrack(nums, perm, res)  # Explore
                    perm.pop()  # Unchoose

    res = []
    perm = []
    backtrack(nums, perm, res)
    
    # Print all permutations
    for perm in res:
        print(perm)
    
    # Return the total number of permutations
    return len(res)