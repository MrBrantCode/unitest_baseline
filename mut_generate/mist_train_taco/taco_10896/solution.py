"""
QUESTION:
In this Kata, you will be given two numbers, n and k and your task will be to return the k-digit array that sums to n and has the maximum possible GCD.

For example, given `n = 12, k = 3`, there are a number of possible `3-digit` arrays that sum to `12`, such as `[1,2,9], [2,3,7], [2,4,6], ...` and so on. Of all the possibilities, the one with the highest GCD is `[2,4,6]`. Therefore, `solve(12,3) = [2,4,6]`.

Note also that digits cannot be repeated within the sub-array, so `[1,1,10]` is not a possibility. Lastly, if there is no such array, return an empty array.

More examples in the test cases.

Good luck!
"""

def find_max_gcd_array(n, k):
    maxGcd = 2 * n // (k * (k + 1))
    for gcd in range(maxGcd, 0, -1):
        last = n - gcd * k * (k - 1) // 2
        if not last % gcd:
            return [gcd * x if x != k else last for x in range(1, k + 1)]
    return []