"""
QUESTION:
Given a number N. The task is to check whether there is pair of adjacent set bit or not in the binary representation of number.
NOTE: If the number has pair of adjacent set bits return "Yes" else return "No".
Example 1:
Input: n = 1
Output: "No" 
Explanation: There is no pair of adjacent 
set bit in the binary representation of 1.
Example 2:
Input: n = 3
Output: "Yes"
Explanation: There is pair of adjacent
set bit present in the binary 
representation of 3(0011).
Your Task:  
You dont need to read input or print anything. Complete the function isAdjacentSetBits() which takes n as input parameter and returns "Yes" If the number has pair of adjacent set bits else "No".
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=10^{11}
"""

def has_adjacent_set_bits(n: int) -> str:
    # Convert the number to its binary representation
    binary_representation = bin(n)[2:]
    
    # Check if there is a pair of adjacent '1's in the binary representation
    if '11' in binary_representation:
        return 'Yes'
    else:
        return 'No'