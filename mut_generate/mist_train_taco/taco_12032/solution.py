"""
QUESTION:
Given a number N, generate bit patterns from 0 to 2^N-1 such that successive patterns differ by one bit. 
A Gray code sequence must begin with 0.
 
Example 1:
Input:
N = 2
Output: 
00 01 11 10
Explanation: 
00 and 01 differ by one bit.
01 and 11 differ by one bit.
11 and 10 also differ by one bit.
 
Example 2:
Input:
N=3
Output:
000 001 011 010 110 111 101 100
Explanation:
000 and 001 differ by one bit.
001 and 011 differ by one bit.
011 and 010 differ by one bit.
Similarly, every successive pattern 
differs by one bit.
Your task:
You don't need to read input or print anything. Your task is to complete the function graycode() which takes an integer N as input and returns a la list of patterns.
 
Expected Time Complexity: O(2^{n})
Expected Auxiliary Space: O(2^{n})
 
Constraints :
1<=N<=16
"""

def generate_gray_code(n: int) -> list[str]:
    if n == 1:
        return ['0', '1']
    
    # Generate Gray code for n-1
    prev_gray_code = generate_gray_code(n - 1)
    
    # Construct the Gray code for n
    gray_code = []
    
    # Add '0' prefix to the previous Gray code
    for code in prev_gray_code:
        gray_code.append('0' + code)
    
    # Add '1' prefix to the reversed previous Gray code
    for code in reversed(prev_gray_code):
        gray_code.append('1' + code)
    
    return gray_code