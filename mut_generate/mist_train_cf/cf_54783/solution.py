"""
QUESTION:
Write a function `checkArithmeticSubarrays(nums, l, r)` that takes in three parameters: `nums`, an array of `n` integers, and two arrays of `m` integers each, `l` and `r`, representing `m` range queries. The function should return a list of boolean elements `answer`, where `answer[i]` is true if the subarray `nums[l[i]], nums[l[i]+1], ... , nums[r[i]]` can be rearranged to form an arithmetic sequence with distinct elements, and false otherwise.

Constraints: 
- `n == nums.length`
- `m == l.length`
- `m == r.length`
- `2 <= n <= 500`
- `1 <= m <= 500`
- `0 <= l[i] < r[i] < n`
- `-10^5 <= nums[i] <= 10^5`
"""

def checkArithmeticSubarrays(nums, l, r):
    res = []
    for start, end in zip(l, r):
        subarray = sorted(nums[start:end+1])
        d = subarray[1] - subarray[0]
        if all(subarray[i] - subarray[i - 1] == d for i in range(2, len(subarray))):
            res.append(True)
        else:
            res.append(False)
    return res