"""
QUESTION:
Given a binary representation in the form of string(S) of a number n, the task is to find a binary representation of n+1.
Example 1:
Input: S = "10"
Output: 11
Explanation: "10" is the binary 
representation of 2 and binary 
representation of 3 is "11"
Example 2:
Input: S = "111"
Output: 1000
Explanation: "111" is the binary 
representation of 7 and binary 
representation of 8 is "1000"
Your Task:  
You don't need to read input or print anything. Complete the function binaryNextNumber()which takes S as input parameter and returns the string.
Expected Time Complexity:O(N)
Expected Auxiliary Space: O(N) to store resultant string  
Constraints:
1 <= N <= 10^{4}
"""

def binary_next_number(S: str) -> str:
    """
    Given a binary representation in the form of string S of a number n, 
    this function returns the binary representation of n+1.

    Parameters:
    S (str): A string representing the binary number.

    Returns:
    str: A string representing the binary number of n+1.
    """
    return bin(int(S, 2) + 1)[2:]