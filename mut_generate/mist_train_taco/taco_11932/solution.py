"""
QUESTION:
Given an even digit number N, partition the number into multiple numbers of two digits. For ex: if he chooses 1345 then he parts the number into 13 and 45. Calculate the product of these two digit numbers modulo (10^{9}+7).
 
Example 1:
Input:
N = 2222
Output:
484
Explanation:
2222 is divided into 22 and 22.
So, the result is 484.
Example 2:
Input:
N = 10
Output:
10
Explanation:
10 can be divided into only 10
so the result is 10. 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function prodTwoDigit() which takes an Integer N as input and returns the product of two digit numbers when N is divided.
 
Expected Time Complexity: O(log_{100}N)
Expected Auxiliary Space: O(1)
 
Constraints:
2 <= N <= 10^{18}
"""

import math

def calculate_two_digit_product(N: int) -> int:
    def nod(n: int) -> int:
        return int(math.log10(n)) + 1

    def two_digit_no_array(N: int) -> list:
        res = []
        prev = N
        curr = N // 100
        while curr != 0:
            res.append(prev - curr * 100)
            prev = curr
            curr = curr // 100
        res.append(prev)
        return res

    m = 1000000007
    if N == 0:
        return 0
    elif nod(N) == 2:
        return N
    else:
        tdl = two_digit_no_array(N)
        prod = 1
        for i in tdl:
            prod = prod * i % m
        return prod