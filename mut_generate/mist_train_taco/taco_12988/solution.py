"""
QUESTION:
Write a program to print Binary representation of a given number N.
Example 1:
Input:
N = 2
Output:
000000000000000000000000000010
Explanation:
The binary representation of 2 is '10'
but we need to print in 30 bits so append
remaining 0's in the left.
Example 2:
Input:
N = 5
Output:
000000000000000000000000000101
Explanation:
The binary representation of 5 is '101'.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getBinaryRep() which takes an Integer N as input parameter and returns a string of size 30 which is the binary representation of N.
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^9
"""

def get_binary_representation(N: int) -> str:
    # Initialize a list with 30 '0's
    binary_rep = ['0' for _ in range(30)]
    
    # Convert the number to binary
    i = 0
    while N:
        if N & 1 == 1:
            binary_rep[30 - i - 1] = '1'
        N >>= 1
        i += 1
    
    # Join the list into a string and return
    return ''.join(binary_rep)