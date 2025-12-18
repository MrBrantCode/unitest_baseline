"""
QUESTION:
Implement a function `robust_median` that takes a list or tuple `l` containing numbers (including potential duplicates, extreme values, and `None` entries representing missing data) and returns the median value. The function should not use built-in sorting or median calculation functions. It should handle cases where the list is empty, has an odd or even number of elements, and contains outliers by filtering them based on the interquartile range (IQR). If the list is empty after removing missing data and outliers, return `None`.
"""

import random

def robust_median(l: list):
    # Removing None entries
    l = [i for i in l if i is not None]

    if len(l) == 0:
        return None

    # Removing outliers
    Q1 = select(l, len(l) // 4, 0, len(l) - 1)
    Q3 = select(l, (len(l) * 3) // 4, 0, len(l) - 1)
    IQR = Q3 - Q1
    l = [i for i in l if Q1 - 1.5 * IQR <= i <= Q3 + 1.5 * IQR]

    if len(l) == 0:
        return None

    if len(l) % 2 == 1:
        return select(l, len(l) // 2, 0, len(l) - 1)
    else:
        return 0.5 * (select(l, len(l) // 2 - 1, 0, len(l) - 1) 
                    + select(l, len(l) // 2, 0, len(l) - 1))

def select(nums, k, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    if k == i + 1:
        return nums[k]
    elif k < i + 1:
        return select(nums, k, low, i)
    else:
        return select(nums, k, i + 1, high)