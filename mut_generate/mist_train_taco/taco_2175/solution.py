"""
QUESTION:
Given a number, the task is to set all odd bits of a number.
NOTE: Position of Least Significant Bit is considered as 1.
Example 1:
Input: n = 20
Output: 21 
Explanation: Binary representation of 20 
is 10100. Setting all odd bits make the 
number 10101 which is binary
representation of 21.
Example 2:
Input: n = 10
Output: 15
Explanation: Binary representation of 10
is 1010. Setting all odd bits make the
number 1111 which is binary representation
of 15.
Your Task:  
You dont need to read input or print anything. Complete the function setAllOddBitsÃ¢â¬â¹() which takes n as input parameter and returns the modified number.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=10^{9}
"""

def set_all_odd_bits(n: int) -> int:
    for i in range(0, 32, 2):
        if 1 << i <= n:
            n |= 1 << i
    return n