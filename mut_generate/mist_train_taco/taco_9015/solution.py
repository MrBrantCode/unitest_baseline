"""
QUESTION:
You are given a number N. Find the total number of setbits in the numbers from 1 to N. 
Example 1:
Input: N = 3
Output: 4
Explaination: 
1 -> 01, 2 -> 10 and 3 -> 11. 
So total 4 setbits.
Example 2:
Input: N = 4
Output: 5
Explaination: 1 -> 01, 2 -> 10, 3 -> 11 
and 4 -> 100. So total 5 setbits.
Your Task:
You do not need to read input or print anything. Your task is to complete the function countBits() which takes N as input parameter and returns the total number of setbits upto N.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{9}
"""

def count_setbits_upto_n(n: int) -> int:
    k = 1
    su = 0
    while n // 2 ** (k - 1) > 0:
        d = n % 2 ** k
        rep = n // 2 ** k
        rep = rep * 2 ** (k - 1)
        if d + 1 - 2 ** (k - 1) > 0:
            su = su + rep + (d + 1 - 2 ** (k - 1))
        else:
            su += rep
        k += 1
    return su