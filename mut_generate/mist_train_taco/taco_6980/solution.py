"""
QUESTION:
Given a non-negative integer n. Reverse the bits of n and print the number obtained after reversing the bits. 
Note:  The actual binary representation of the number is being considered for reversing the bits, no leading 0’s are being considered.
 
Example 1:
Input : 
N = 11
Output:
13
Explanation:
(11)_{10} = (1011)_{2}.
After reversing the bits we get:
(1101)_{2} = (13)_{10}.
Example 2:
Input : 
N = 10
Output:
5
Explanation:
(10)_{10} = (1010)_{2}.
After reversing the bits we get:
(0101)_{2} = (101)_{2}
        = (5)_{10}.
Your task:
You don't need to read input or print anything. Your task is to complete the function reverseBits() which takes an integer N as input and returns the number obtained after reversing bits.
 
Expected Time Complexity : O(number of bits in the binary representation of N)
Expected Auxiliary Space :  O(1)
 
Constraints :
1 ≤ N ≤ 10^{9}
"""

def reverse_bits(n: int) -> int:
    # Convert the integer to its binary representation, excluding the '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Reverse the binary string
    reversed_binary_representation = binary_representation[::-1]
    
    # Convert the reversed binary string back to an integer
    reversed_number = int(reversed_binary_representation, 2)
    
    return reversed_number