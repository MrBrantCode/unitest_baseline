"""
QUESTION:
Given a non-negative number N and two values L and R. The problem is to set all the bits in the range L to R in the binary representation of N.
Example 1:
Input :
N = 17, L = 2, R = 3 
Output :
23
Explanation:
(17)_{10} = (10001)_{2}
(23)_{10} = (10111)_{2}
The bits in the range 2 to 3 in the binary
representation of 17 are set.
Example 2:
Input :
N = 8, L = 1, R = 2 
Output :
11
Explanation:
(8)_{10} = (1000)_{2}
(11)_{10} = (1011)_{2}
The bits in the range 2 to 3 in the binary
representation of 8 are set.
Your Task:
You don't need to read input or print anything. Your task is to complete the function setAllRangeBits() which takes an Integer N as input and returns the answer.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{8}
"""

def set_all_range_bits(N: int, L: int, R: int) -> int:
    for i in range(L - 1, R):
        N = N | (1 << i)
    return N