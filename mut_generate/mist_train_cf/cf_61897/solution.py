"""
QUESTION:
You are given two arrays of equal length, `target` and `initial`, where `target` consists of positive integers and `initial` is filled with zeros. Your task is to determine the minimum number of operations required to transform `initial` into `target` by selecting any subarray from `initial` and incrementing each value in it by one. The `minNumberOperations` function should return this minimum number of operations. The constraints are: `1 <= target.length <= 10^5` and `1 <= target[i] <= 10^5`.
"""

def minNumberOperations(target):
    operations = target[0]
    for i in range(1, len(target)):
        if target[i] > target[i-1]:
            operations += target[i] - target[i - 1]
    return operations