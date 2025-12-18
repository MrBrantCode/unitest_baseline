"""
QUESTION:
Given a number N.Find the sum of fifth powers of natural numbers till N i.e. 1^{5}+2^{5}+3^{5}+..+N^{5}.
Example 1:
Input:
N=2
Output:
33
Explanation:
The sum is calculated as 1^{5}+2^{5}=1+32=33.
Example 2:
Input:
N=3
Output:
276
Explanation:
The sum is calculated as 1^{5}+2^{5}+3^{5}
=1+32+243=276.
Your Task:
You don't need to read input or print anything.Your task is to complete the function sumOfFifthPowers() which takes an integer N as input parameter and returns the sum of the fifth powers of Natural numbers till N.
Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=1000
"""

def sum_of_fifth_powers(n: int) -> int:
    return n * n * (n + 1) * (n + 1) * (2 * n * n + 2 * n - 1) // 12