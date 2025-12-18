"""
QUESTION:
Given a non-negative number N and two values L and R. The problem is to toggle the bits in the range L to R in the binary representation of N, i.e, to toggle bits from the rightmost Lth bit to the rightmost Rth bit. A toggle operation flips a bit 0 to 1 and a bit 1 to 0. Print N after the bits are toggled.
 
Example 1:
Input:
N = 17 , L = 2 , R = 3
Output:
23
Explanation:
(17)_{10} = (10001)_{2}.  After toggling all
the bits from 2nd to 3rd position we get
(10111)_{2} = (23)_{10}
Example 2:
Input:
N = 50 , L = 2 , R = 5
Output:
44
Explanation:
(50)_{10} = (110010)_{2}.  After toggling all
the bits from 2nd to 5th position we get
(101100)_{2} = (44)_{10}
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function toggleBits() which takes 3 Integers N,L and R as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
1 <= L<=R <=^{ }Number of Bits in N
"""

def toggle_bits(N: int, L: int, R: int) -> int:
    # Convert N to its binary representation as a string
    binary_str = bin(N)[2:]
    
    # Convert the binary string to a list of characters for easy manipulation
    binary_list = list(binary_str)
    
    # Calculate the starting and ending indices for the range to toggle
    start_index = len(binary_list) - L
    end_index = len(binary_list) - R
    
    # Toggle the bits in the specified range
    for i in range(start_index, end_index + 1):
        if binary_list[i] == '1':
            binary_list[i] = '0'
        else:
            binary_list[i] = '1'
    
    # Join the list back into a string and convert it to an integer
    toggled_binary_str = ''.join(binary_list)
    result = int(toggled_binary_str, 2)
    
    return result