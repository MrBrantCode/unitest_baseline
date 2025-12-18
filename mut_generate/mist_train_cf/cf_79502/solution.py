"""
QUESTION:
Given an integer `n` representing the length of the array and an integer `m`, return the minimum number of operations needed to make all elements of the array `arr`, where `arr[i] = (2 * i) + 1`, equal. The operation can select two indices `x` and `y` and subtract `1` from `arr[x]` and add `1` to `arr[y]`. However, the same index cannot be selected more than `m` times. If it is not possible to make all elements equal with this constraint, return -1.

Constraints: `1 <= n <= 10^4` and `1 <= m <= n`.
"""

def entrance(n: int, m: int) -> int:
    average = n
    operations = 0
    for i in range(n):
        value = (2 * i) + 1
        required_operations = (average - value) // 2
        if required_operations > m:
            return -1
        operations += required_operations
    return operations