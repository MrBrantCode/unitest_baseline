"""
QUESTION:
Given a number N. The task is to check whether it is sparse or not. A number is said to be a sparse number if no two or more consecutive bits are set in the binary representation.
Example 1:
Input: N = 2
Output: 1
Explanation: Binary Representation of 2 is 10, 
which is not having consecutive set bits. 
So, it is sparse number.
Example 2:
Input: N = 3
Output: 0
Explanation: Binary Representation of 3 is 11, 
which is having consecutive set bits in it. 
So, it is not a sparse number.
Your Task: The task is to complete the function checkSparse() that takes n as a parameter and returns 1 if the number is sparse else returns 0.
Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).
Constraints:
1 <= N <= 10^{6}
"""

def is_sparse(n: int) -> int:
    # Convert the number to its binary representation and remove the '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Split the binary representation by '0' to find consecutive '1's
    parts = binary_representation.split('0')
    
    # Check if any part has more than one '1'
    for part in parts:
        if len(part) > 1:
            return 0
    
    return 1