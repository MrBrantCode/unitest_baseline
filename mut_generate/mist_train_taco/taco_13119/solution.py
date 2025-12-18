"""
QUESTION:
Given a number N. Find the product of the number of setbits and the number itself.
Example 1:
Input: N = 2
Output: 2
Explaination: 2 has one setbit. So, 2*1 = 2.
Example 2:
Input: N = 3
Output: 6
Explaination: 3 has 2 setbits. 3*2 = 6.
Your Task:
You do not need to read input or print anything. Your task is to complete the function bitMultiply() which takes the number N as input parameters and returns the product.
Expected Time Complexity: O(Log N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{6}
"""

def bit_multiply(N: int) -> int:
    # Convert the number to its binary representation and remove the '0b' prefix
    binary_representation = bin(N).replace('0b', '')
    
    # Count the number of set bits (1s) in the binary representation
    set_bit_count = binary_representation.count('1')
    
    # Calculate the product of the number of set bits and the number itself
    result = set_bit_count * N
    
    return result