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
 
Expected Time Complexity : O(log N)
Expected Auxiliary Space : O(1)
 
Constraints :
0 <= A, B <= 10^{9}
"""

def find_min_xor_with_set_bits(A: int, B: int) -> int:
    # Convert A to binary string without the '0b' prefix
    a_bin = bin(A)[2:]
    
    # Count the number of set bits in B
    count_b_set_bits = bin(B).count('1')
    
    # Initialize a list to represent the binary string of X
    x_bin = ['0' for _ in range(len(a_bin))]
    
    # First pass: Set bits in X where A has bits to minimize XOR
    for i in range(len(a_bin)):
        if a_bin[i] == '1' and count_b_set_bits > 0:
            x_bin[i] = '1'
            count_b_set_bits -= 1
    
    # Second pass: Set remaining bits from the least significant bit
    for i in range(len(x_bin) - 1, -1, -1):
        if x_bin[i] == '0' and count_b_set_bits > 0:
            x_bin[i] = '1'
            count_b_set_bits -= 1
    
    # If there are still set bits left to be added, append them to the most significant side
    if count_b_set_bits > 0:
        x_bin.reverse()
        while count_b_set_bits:
            x_bin.append('1')
            count_b_set_bits -= 1
        x_bin.reverse()
    
    # Convert the binary string back to an integer
    x_value = 0
    for i in range(len(x_bin)):
        if x_bin[i] == '1':
            x_value += 1 << (len(x_bin) - 1 - i)
    
    return x_value