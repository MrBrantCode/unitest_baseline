"""
QUESTION:
Given two arrays of integers `arr1` and `arr2` of equal length `n`, where `2 <= n <= 40000`, and all elements in both arrays are distinct and within the range `-10^6 <= arr1[i], arr2[i] <= 10^6`, write a function `max_abs_val_expr(arr1, arr2)` to find the maximum value of `|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|` for all `0 <= i, j < n`. The function should not sort the input arrays before performing the operation.
"""

def max_abs_val_expr(arr1, arr2):
    n = len(arr1)
    ans1, ans2, ans3, ans4 = -float('inf'), -float('inf'), -float('inf'), -float('inf')
    min1, min2, min3, min4 = float('inf'), float('inf'), float('inf'), float('inf')

    for i in range(n):
        ans1 = max(ans1, arr1[i] + arr2[i] + i)
        ans2 = max(ans2,-arr1[i] + arr2[i] + i)
        ans3 = max(ans3, arr1[i] - arr2[i] + i)
        ans4 = max(ans4, -arr1[i] - arr2[i] + i)

        min1 = min(min1, arr1[i] + arr2[i] + i)
        min2 = min(min2,-arr1[i] + arr2[i] + i)
        min3 = min(min3, arr1[i] - arr2[i] + i)
        min4 = min(min4, -arr1[i] - arr2[i] + i)

    return max(ans1-min1, ans2-min2, ans3-min3, ans4-min4)