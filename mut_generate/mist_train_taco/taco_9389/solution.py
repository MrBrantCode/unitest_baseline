"""
QUESTION:
Polycarpus loves lucky numbers. Everybody knows that lucky numbers are positive integers, whose decimal representation (without leading zeroes) contain only the lucky digits x and y. For example, if x = 4, and y = 7, then numbers 47, 744, 4 are lucky.

Let's call a positive integer a undoubtedly lucky, if there are such digits x and y (0 ≤ x, y ≤ 9), that the decimal representation of number a (without leading zeroes) contains only digits x and y.

Polycarpus has integer n. He wants to know how many positive integers that do not exceed n, are undoubtedly lucky. Help him, count this number.


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 10^9) — Polycarpus's number.


-----Output-----

Print a single integer that says, how many positive integers that do not exceed n are undoubtedly lucky.


-----Examples-----
Input
10

Output
10

Input
123

Output
113



-----Note-----

In the first test sample all numbers that do not exceed 10 are undoubtedly lucky.

In the second sample numbers 102, 103, 104, 105, 106, 107, 108, 109, 120, 123 are not undoubtedly lucky.
"""

def count_undoubtedly_lucky_numbers(n: int) -> int:
    nset = set()

    def resolve(x, y, num, flag):
        if num > n or (flag and num == 0):
            return
        if num > 0:
            nset.add(num)
        resolve(x, y, num * 10 + x, True)
        resolve(x, y, num * 10 + y, True)

    for i in range(10):
        for j in range(i + 1, 10):
            resolve(i, j, 0, False)

    return len(nset)