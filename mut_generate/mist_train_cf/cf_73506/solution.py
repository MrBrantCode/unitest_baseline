"""
QUESTION:
Create a function called `numsSameConsecutiveDifference` that generates all non-negative integers of length `n` where the absolute difference between each pair of successive digits is `k`. Any number in the output should not commence with zeros. The function should take two parameters, `n` and `k`, where `2 <= n <= 9` and `0 <= k <= 9`.
"""

def numsSameConsecutiveDifference(n: int, k: int) -> [int]:
    if n == 1: 
        return [i for i in range(10)]  
    res = [i for i in range(1, 10)]
    for _ in range(n - 1):
        temp = []
        for num in res:
            if num % 10 + k < 10:
                temp.append(num * 10 + num % 10 + k)
            if k > 0 and num % 10 - k >= 0:
                temp.append(num * 10 + num % 10 - k)
        res = temp
    return res