"""
QUESTION:
Given two numbers N and K, change the Kth (1-based indexing) bit from the left of the binary representation of the number N to '0' if it is  '1', else return the number N itself.
Example 1:
Input:
N = 13, K = 2
Output: 9
Explanation: Binary representation of 13 is
1101. The 2nd bit from left is 1, we make
it 0 and result is 1001 = 9 (decimal).
Example 2:
Input: 
N = 13, K = 6
Output: 13
Explanation: Binary representation of 13 is
1101. There's no 6th bit from left,
hence we return the number itself.
Your Task:
You don't need to read input or print anything. Your task is to complete the function replaceBit() which takes the integers N and K as inputs and returns the resultant number after the stated modifications.
Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(1).
Constraints:
1<=N<=10^{6}
"""

def replace_kth_bit(N: int, K: int) -> int:
    # Convert the integer N to its binary representation as a list of characters
    binary_representation = list(bin(N)[2:])
    
    # Check if K is within the bounds of the binary representation
    if len(binary_representation) >= K:
        # Calculate the 0-based index from the 1-based K
        index = K - 1
        
        # Check if the bit at the index is '1'
        if binary_representation[index] == '1':
            # Change the bit to '0'
            binary_representation[index] = '0'
            # Convert the modified binary representation back to an integer
            return int(''.join(binary_representation), 2)
    
    # If K is out of bounds or the bit is already '0', return the original number
    return N