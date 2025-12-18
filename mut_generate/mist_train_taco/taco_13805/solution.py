"""
QUESTION:
Given a number N, the task is to find XOR of count of 0s and count of 1s in binary representation of a given number.
 
Example 1:
Input: N = 5
Output: 3
Explanation: 
Binary representation: 101
Set_bit_count: 2
Unset_bit_count: 1
2 XOR 1 = 3
Example 2:
Input: N = 7
Output: 3
Expalanation:
Binary representation: 111
Set_bit_count: 3
Unset_bit_count: 0
3 XOR 0 = 3
Your Task:
You don't need to read or print anything. Your task is to complete the function find_xor() which takes N as input parameter and returns the XOR of count of 0s and count of 1s in binary representation of N.
Expected Time Complexity: O(log(N))
Expected Space Complexity: O(1)
Constranits:
1 <= N <= 10^{9}
"""

def find_xor(n: int) -> int:
    # Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Count the number of '1's and '0's in the binary representation
    count_of_ones = binary_representation.count('1')
    count_of_zeros = binary_representation.count('0')
    
    # Return the XOR of the counts
    return count_of_ones ^ count_of_zeros