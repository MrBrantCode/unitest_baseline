"""
QUESTION:
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.


Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)



Examples: 

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

def minimize_largest_sum(nums, m):
    def is_splitable(accum, m, maxx):
        start = 0
        N = len(accum)
        end = 0
        count = 0
        while end < N and count < m:
            if accum[end] - accum[start] > maxx:
                start = end - 1
                count += 1
            end += 1
        if accum[-1] - accum[start] > maxx:
            count += 2
        else:
            count += 1
        if end != N or count > m:
            return False
        return True

    accum = [0]
    N = len(nums)
    mmm = max(nums)
    if m >= N:
        return mmm
    res = 0
    for i in nums:
        res += i
        accum.append(res)
    (lower, upper) = (mmm, sum(nums))
    while lower < upper:
        mid = (lower + upper) // 2
        if not is_splitable(accum, m, mid):
            lower = mid + 1
        else:
            upper = mid
    return upper