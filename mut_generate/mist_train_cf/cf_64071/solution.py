"""
QUESTION:
Given an integer `n`, calculate the number of potential attendance records of length `n` that qualify a student for an attendance award. The attendance record can be one of three characters: `'A'` for absence, `'L'` for lateness, or `'P'` for presence. To qualify for an attendance award, the student must have been absent less than 2 days and never late for 3 or more successive days. Return the result modulo `10^9 + 7`.

The input `n` is an integer where `1 <= n <= 10^5`.
"""

def checkRecord(n: int) -> int:
    mod = 10**9 + 7
    if n == 1: return 3
    if n == 2: return 8
    arr  = [0, 1, 1, 3, 8, 19]
    sums = [0, 3, 6, 11, 21, 43]
    for i in range(5, n):
        tmp = (sums[i-2] + arr[i-2] + arr[i-1]) % mod
        arr.append(tmp)
        sums.append((sums[i-1] + tmp) % mod)
    
    return ((sums[n-1] + arr[n-1] + arr[n-2]) % mod)