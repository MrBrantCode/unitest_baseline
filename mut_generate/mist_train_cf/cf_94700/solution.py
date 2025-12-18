"""
QUESTION:
Write a function `find_pairs(nums, target_sum)` that takes a list of integers `nums` and an integer `target_sum` as input. The function should return all unique pairs of numbers in `nums` whose sum is equal to `target_sum`. The pairs should be returned in ascending order based on the first element of each pair. If a pair has two identical elements, it should be excluded from the result.
"""

def find_pairs(nums, target_sum):
    pairs = set()
    count = {}
    
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in nums:
        difference = target_sum - num
        if difference in count and count[difference] > 0 and difference != num:
            pairs.add((min(num, difference), max(num, difference)))
            count[difference] -= 1

    return sorted(pairs, key=lambda x: x[0])