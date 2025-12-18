"""
QUESTION:
Write a function named `splitArray` that takes an array of integers as input and returns `True` if there exist quadruplets `(i, j, k, l)` such that the cumulative sum of the subarrays `(0, i - 1)`, `(i + 1, j - 1)`, `(j + 1, k - 1)`, `(k + 1, l - 1)`, and `(l + 1, n - 1)` are identical, and `False` otherwise. The input array will have a length `n` where `1 <= n <= 5000`, and the elements will be within the range `[-1,000,000, 1,000,000]`.
"""

def splitArray(nums):
    n = len(nums)
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    sums = {}

    for j in range(2, n - 2):
        sums.clear()
        for i in range(1, j):
            sum1 = prefix[i]
            sum2 = prefix[j] - prefix[i + 1]
            if sum1 == sum2:
                if sum1 in sums:
                    sums[sum1].append((i, j))
                else:
                    sums[sum1] = [(i, j)]
        for k in range(j + 2, n - 1):
            sum3 = prefix[k] - prefix[j + 1]
            sum4 = prefix[n] - prefix[k + 1]
            if sum3 == sum4 and sum3 in sums:
                for i, _ in sums[sum3]:
                    if i != k:
                        return True
    return False