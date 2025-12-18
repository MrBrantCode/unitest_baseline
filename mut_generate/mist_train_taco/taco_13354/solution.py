"""
QUESTION:
How many n-digit numbers (without leading zeros) are there such that no digit occurs more than k times?  

As the count of such n-digit numbers can be very large, print the answer mod (10^{9}+7)  

Input Format  

The first line contains an integer, T , the number of test cases. This is followed by T lines each containing 2 space separated integers, n and k  

Constraints  

T ≤ 100000 

1 ≤ n ≤ 1000 

1 ≤ k ≤ 10^{9}

Sample Input

2
2 3
2 1

Sample Output

90
81

Explanation 

Case 1: A number can appear three times. So we have 9 (all except 0) numbers for first digit and 10 numbers for the second digit. 

Case 2: A number can appear only once. So we have 9 choices for the first digit and 9(all except the first one) for the second digit.
"""

from math import factorial

def choose(n, k):
    total = factorial(n) // factorial(k)
    total = total // factorial(n - k)
    return int(total)

def incl(n, k, i):
    total = 1
    for j in range(0, i):
        total = (10 - j) * total * choose(n - j * k, k)
    return total

def excl(n, k, i):
    total = choose(n - 1, k - 1)
    for j in range(1, i):
        total = (10 - j - 1) * total * choose(n - j * k, k)
    return total

def count_n_digit_numbers(n, k):
    k += 1  # Adjust k as per the original code logic
    total = 10 ** n - 10 ** (n - 1)
    i = 1
    while n >= i * k:
        if i % 2 == 1:
            total = total - incl(n, k, i) + excl(n, k, i)
        else:
            total = total + incl(n, k, i) - excl(n, k, i)
        i += 1
    return total % (10 ** 9 + 7)