"""
QUESTION:
Write a function `maximumPossible(num, k)` that takes a string `num` and an integer `k` as input, and returns the maximum integer that can be obtained by swapping any two adjacent digits of the integer at most `k` times. The function should return the result as a string. The input string `num` has a length between 1 and 30000, contains only digits, and does not have leading zeros. The value of `k` is between 1 and 10^9.
"""

def maximumPossible(num, k):
    num = list(num)
    i = 0
    while k > 0 and i < len(num):
        max_idx = -1
        for j in range(i + 1, len(num)):
            if j - i > k:
                break
            if max_idx < 0 or num[j] > num[max_idx]:
                max_idx = j

        if num[max_idx] > num[i]:
            temp = num[max_idx]
            for j in range(max_idx, i, -1):
                num[j] = num[j - 1]
            num[i] = temp
            k -= max_idx - i

        i += 1

    return ''.join(num)