"""
QUESTION:
Given a number N, change all bits at even positions to 0.
Example 1:
Input: N = 30
Output: 10 
Explanation: Binary representation of 
11110. Bits at Even positions are 
highlighted. After making all of them 
0, we get 01010. Hence the answer is 10.
Example 2:
Input:  N = 10
Output: 10
Explanation: Binary representation of 
1010. Bits at Even positions are 
highlighted. After making all of them 
0, we get 1010. Hence the answer is 10.
Your Task:  
You dont need to read input or print anything. Complete the function convertEvenBitToZero() which takes n as input parameter and returns the value of N after changing bits at even positions.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=(32-bit number)
"""

def convert_even_bit_to_zero(n: int) -> int:
    num = 2863311530  # This is a bitmask where all even bits are set to 1 and odd bits are set to 0
    return num & n