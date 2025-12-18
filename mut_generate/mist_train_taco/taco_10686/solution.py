"""
QUESTION:
Given two integers A and B, the task is to find an integer X such that (X XOR A) is minimum possible and the count of set bit in X is equal to the count of set bits in B.
Example 1:
Input: 
A = 3, B = 5
Output: 3
Explanation:
Binary(A) = Binary(3) = 011
Binary(B) = Binary(5) = 101
The XOR will be minimum when x = 3
i.e. (3 XOR 3) = 0 and the number
of set bits in 3 is equal
to the number of set bits in 5.
Example 2:
Input: 
A = 7, B = 12
Output: 6
Explanation:
(7)_{2}= 111
(12)_{2}= 1100
The XOR will be minimum when x = 6 
i.e. (6 XOR 7) = 1 and the number 
of set bits in 6 is equal to the 
number of set bits in 12.
Your task :
You don't need to read input or print anything. Your task is to complete the function minVal() that takes integer A and B as input and returns the value of X according to the question.
 
Expected Time Complexity : O(log MAX(A,B))
Expected Auxiliary Space : O(1)
 
Constraints :
1 <= A, B <= 10^{9}
"""

def find_min_xor_with_set_bits(A: int, B: int) -> int:
    # Count the number of set bits in B
    num_set_bits_b = bin(B)[2:].count('1')
    
    # Convert A to its binary representation and store it as a list of characters
    a_bin_arr = list(bin(A)[2:])
    
    # Initialize the result binary string
    ans = ''
    
    # Iterate over the binary representation of A
    for bit in a_bin_arr:
        if bit == '1' and num_set_bits_b > 0:
            # If the bit is '1' and we still need more set bits, set the corresponding bit in ans to '1'
            num_set_bits_b -= 1
            ans += '1'
        else:
            # Otherwise, set the corresponding bit in ans to '0'
            ans += '0'
    
    # Convert ans to a list for easier manipulation
    ans = list(ans)
    
    # If there are still set bits needed, add them to the least significant positions
    i = 1
    while num_set_bits_b > 0:
        if a_bin_arr[-i] != '1':
            # If the corresponding bit in A is not '1', set the bit in ans to '1'
            ans[-i] = '1'
            num_set_bits_b -= 1
        i += 1
    
    # Convert the binary string back to an integer
    ans = ''.join(ans)
    return int(ans, 2)