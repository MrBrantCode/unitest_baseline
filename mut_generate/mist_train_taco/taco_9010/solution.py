"""
QUESTION:
Given a number N, complete the following tasks,
Task 1. Generate a new number from N by changing the zeroes in the binary representation of N to 1.
Task  2. Find the difference between N and the newly generated number.
 
Example 1: 
Input: N = 8 
Output: 7 15
Explanation:
There are 3 zeroes in binary representation
of 8. Changing them to 1 will give 15.
Difference between these two is 7.
Example 2: 
Input: N = 6 
Output: 1 7
Explanation:
There is 1 zero in binary representation
of 6. Changing it to 1 will give 7.
Difference between these two is 1.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function changeBits() which takes an integer N as input parameter and returns a list of two integers containing the difference and the generated number respectively.
 
Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)
 
Constraints:
0 <= N <= 10^{8}
"""

def change_bits(N: int) -> tuple:
    # Calculate the number of bits required to represent N
    num_bits = N.bit_length()
    
    # Generate the new number by setting all bits to 1
    new_number = (1 << num_bits) - 1
    
    # Calculate the difference between the new number and the original number
    difference = new_number - N
    
    # Return the difference and the new number
    return (difference, new_number)