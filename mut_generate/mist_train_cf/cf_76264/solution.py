"""
QUESTION:
Create a function `euler_totient_range(start, end)` that takes two integers `start` and `end` as input, representing a range of numbers. Using a backtracking algorithm and incorporating concepts of greedy theory, the function should calculate and return a dictionary containing the Euler's Totient values for every number from `start` to `end` (inclusive). Note that the use of backtracking may not be the most efficient approach for this problem.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def euler_totient(n):
    if n == 1:
        return 1
    else:
        count = 0
        for x in range(1, n + 1):
            if gcd(n, x) == 1:
                count += 1
        return count


def euler_totient_range(start, end):
    totient_values = {}
    for i in range(start, end + 1):
        totient_values[i] = euler_totient(i)
    return totient_values