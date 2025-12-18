"""
QUESTION:
Given a list of 32 bit unsigned integers N. Find X, the unsigned integer you get by flipping bits in the binary representation of N. i.e. unset bits must be set, and set bits must be unset. Also find the binary representation of X in reverse order.
Example 1:
Input: N = 1
Output: 4294967294 01111111111111111111111111111111
Explaination: 
1 as unsigned 32-bits is 00000000000000000000000000000001. 
Flipping its bits we get 11111111111111111111111111111110.
Its binary representation is 4294967294.
Its reverse order is 01111111111111111111111111111111.
 
Example 2:
Input: N = 2
Output: 4294967293 10111111111111111111111111111111
Explaination: 
2 as unsigned 32-bits is 00000000000000000000000000000010. 
Flipping its bits we get 11111111111111111111111111111101.
Its binary representation is 4294967293.
Its reverse order is 1011111111111111111111111111111.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function flipBits() which takes N as input parameter and returns a list of strings containing two values, X and  binary representation of X in reverse order.
 
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(logN)
 
Constraints:
1 ≤ N < 4294967296
"""

def flip_bits(N: int) -> tuple:
    # Calculate the flipped number
    num = 4294967295 - N
    
    # Get the binary representation of the flipped number
    binary_num = bin(num)[2:]
    
    # Reverse the binary representation and pad with leading zeros to ensure 32 bits
    reversed_binary = ''.join(reversed(['0'] * (32 - len(binary_num)) + list(binary_num)))
    
    # Return the result as a tuple
    return (num, reversed_binary)