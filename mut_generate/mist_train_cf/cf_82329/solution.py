"""
QUESTION:
Create a function `find_best_combo(target, numbers, perms, repeats)` that calculates the optimal combination of numbers that minimizes the difference when subtracted from the target. The function should consider the repetition of numbers, permutations, and return an array including the minimum difference and the combination that gave the minimum difference. The target, numbers, and perms should be integers, and repeats should be a boolean value indicating whether numbers can repeat or not.
"""

from itertools import permutations

def find_best_combo(target, numbers, perms, repeats):
    if not repeats:
        numbers = list(set(numbers)) # remove duplicates if repeats not allowed
    all_nums = []
    for i in range(1, perms + 1):
        all_nums.extend(permutations(numbers, i)) # generate permutations of length 1 to perms
    all_sums = [(abs(sum(num) - target), num) for num in all_nums] # calculate all differences
    all_sums.sort() # sort by difference
    return list(all_sums[0]) # return combo with smallest difference