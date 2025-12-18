"""
QUESTION:
Given a number N. Check if it is a Kaprekar number or not.
Note:- A Kaprekar number is a number whose square when divided into two parts the sum of those parts is equal to the original number and none of the parts has value 0. Now given a number, your task is to check if it is Kaprekar number or not.
Example 1:
Input:
N=45
Output:
1
Explanation:
45*45=2025. Now, 20+25=45.
Thus, 45 is a kaprekar number.
Example 2:
Input:
N=20
Output:
0
Explanation:
20*20=400.There is no way to divide
400 into two parts such that their sum is equal
to 20.So, 20 is not a kaprekar number.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function isKaprekar() which takes the number N as input parameter and returns 1 if N is a kaprekar number.Otherwise, it returns 0.
Expected Time Complexity:O(LogN)
Expected Auxillary Space:O(1) 
Constraints:
1<=N<=10^{4}
"""

import math

def is_kaprekar(N):
    sn = N * N
    nod = int(math.log10(sn)) + 1
    dn = sn
    temp = 0
    i = 0
    
    while i != nod // 2:
        temp = sn % 10 * 10 ** i + temp
        sn = sn // 10
        i += 1
    
    if sn != 0 and temp != 0 and (sn + temp == N):
        return 1
    return 0