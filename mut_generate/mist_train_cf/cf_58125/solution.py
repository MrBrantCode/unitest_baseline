"""
QUESTION:
Given an integer `n` and a target digit sum `t`, group numbers from `1` to `n` according to the sum of their digits. Return how many groups have the largest size and their digit sum equals to `t`. 

Function name: `countLargestGroup`

Input: `n` and `t`, where `1 <= n <= 10^4` and `1 <= t <= 9`.

Output: The number of groups with the largest size and digit sum equal to `t`.
"""

def countLargestGroup(n, t):
    def digitSum(num):
        return sum(int(digit) for digit in str(num))

    group_dict = {}

    for i in range(1, n+1):
        group_dict[digitSum(i)] = group_dict.get(digitSum(i), []) + [i]

    max_group_len = max(len(group) for group in group_dict.values())
    target_groups = [group for group in group_dict.values() if len(group) == max_group_len and digitSum(group[0]) == t]

    return len(target_groups)