"""
QUESTION:
Write a function `majorityElement` that takes a list of integers `nums` as input and returns a dictionary where the keys are the elements that appear more than `⌊ n/3 ⌋` times in the list and the values are their respective counts. The function should run in linear time and use O(1) space, excluding the space required for the output. The length of `nums` is between 1 and 5 * 10^4, and the elements in `nums` are between -10^9 and 10^9.
"""

def majorityElement(nums):
    count1, count2, candidate1, candidate2 = 0, 0, None, None

    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1-1, count2-1

    result = {}
    for n in (candidate1, candidate2):
        if nums.count(n) > len(nums) // 3:
            result[n] = nums.count(n)
    return result