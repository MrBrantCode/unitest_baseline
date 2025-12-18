"""
QUESTION:
Given a positive integer n. The problem is to check whether only the first and last bits are set in the binary representation of n. The answer is 1 if the first and last bit is set else 0.
Example 1:
Input: N = 9
Output: 1
Explanation: (9)_{10} = (1001)_{2}, only 
the first and last bits are set.
â€‹Example 2:
Input: N = 15
Output: 0
Explanation: (15)_{10} = (1111)_{2}, except 
first and last there are other bits also
which are set.
Your Task:  
Your task is to complete the function onlyFirstAndLastAreSet() which takes the N as inputs and returns the answer.
Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{9}
"""

def only_first_and_last_bits_set(n: int) -> int:
    # Convert the number to its binary representation as a string
    binary_str = bin(n).replace('0b', '')
    
    # Check if the first and last bits are '1' and there are exactly two '1's in total
    if binary_str[0] == '1' and binary_str[-1] == '1' and binary_str.count('1') == 2:
        return 1
    return 0