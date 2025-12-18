"""
QUESTION:
Given an non-negative integer n. You are only allowed to make set bit unset. You have to find the maximum possible value of query so that after performing the given operations, no three consecutive bits of the integer query are set-bits. 
Example 1:
Input:
n = 2
Output: 
2
Explanation: 
2's binary form is 10, no 3 consecutive set bits are here. 
So, 2 itself would be answer.
Example 2:
Input:
n = 7
Output: 
6
Explanation: 
7's binary form is .....00111.We can observe that 3
consecutive bits are set bits. This is not allowed.
So, we can perfrom the operation of changing set 
bit to unset bit. Now, the number 
becomes 6 that is .....00110. It satifies the 
given condition. Hence, the maximum possible 
value is 6.
Your Task:   You don't need to read input or print anything. Your task is to complete the function noConseBits(), which takes integer n as input parameter and returns the maximum value possible so that it satifies the given condition.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
0 ≤ n ≤ 10^{9}
"""

def noConseBits(n: int) -> int:
    # Convert the integer to its binary representation as a string
    n_bin = bin(n)[2:]
    
    # Initialize the result binary string with the input binary string
    result_bin = n_bin
    
    # Iterate through the binary string
    i = 0
    while i <= len(n_bin) - 3:
        # Check for three consecutive '1's
        if n_bin[i:i + 3] == '111':
            # If found, change the third '1' to '0'
            result_bin = result_bin[:i + 2] + '0' + result_bin[i + 3:]
            # Update the binary string to the modified one
            n_bin = result_bin
        i += 1
    
    # Convert the modified binary string back to an integer
    return int(result_bin, 2)