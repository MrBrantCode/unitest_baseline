"""
QUESTION:
Find the Nth term of the following series :
N    Nth term
1    0
2    1
3    0
4    2
5    0
6    1
7    0
8    3
9    0
10    1
and so on.......
Example 1:
Input: N = 8
Output: 3 
Explanation: According to the series
for N = 8 Nth term is 3.
Example 2:
Input: N = 5
Output: 0
Explanation: According to the series
for N = 5 Nth term is 0.
Your Task:  
You dont need to read input or print anything. Complete the function findNth() which takes N as input parameter and returns the Nth term.
Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=10^{9}
"""

def find_nth_term(n: int) -> int:
    ans = 0
    while n:
        if n & 1:
            return ans
        else:
            ans += 1
            n >>= 1
    return -1