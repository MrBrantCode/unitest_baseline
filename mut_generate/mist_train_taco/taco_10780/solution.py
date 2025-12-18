"""
QUESTION:
Given a series of numbers  6, 14, 36, 98, 276... Identify the pattern in the series and help to identify the integer at Nth index. Indices are starting from 1.
Note: Calculate the answer modulo (10^{9}+7).
 
Example 1:
Input:
N = 2
Output:
14
Explanation:
14 is the 2nd integer of the Series.
Example 2:
Input:
N = 8
Output:
6818
Explanation:
6818 is the 8th integer of the Series.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findNthNum() which takes an Integer N as input and returns the Nth number of the given Series.
 
Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def find_nth_num(N: int) -> int:
    mod = 10**9 + 7
    p1, p2, p3 = 1, 1, 1
    
    for _ in range(N):
        p2 = p2 * 2 % mod
        p3 = p3 * 3 % mod
    
    return ((p1 + p2) % mod + p3) % mod