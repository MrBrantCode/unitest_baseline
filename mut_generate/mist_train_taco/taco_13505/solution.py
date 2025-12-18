"""
QUESTION:
Given a binary representation in the form of string(S) of a number n, the task is to find a binary representation of n-1.
Note: n is greater than zero. 
Example 1:
Input: S = "11"
Output: 10
Explanation: "11" is the binary 
representation of 3 and binary 
representation of 2 is "10"
Example 1:
Input: S = "1000"
Output: 111
Explanation: "1000" is the binary 
representation of 8 and binary 
representation of 7 is "111"
Your Task:  
You don't need to read input or print anything. Complete the function binaryPreviousNumber() which takes S as input parameter and returns the string.
Expected Time Complexity:O(N)
Expected Auxiliary Space: O(N) to store resultant string  
Constraints:
1 <= N <= 10^{4}
"""

def binary_previous_number(S: str) -> str:
    """
    Given a binary representation in the form of string S of a number n, 
    this function returns the binary representation of n-1.

    Parameters:
    S (str): A string representing the binary representation of a number n.

    Returns:
    str: A string representing the binary representation of n-1.
    """
    n = int(S, 2)  # Convert the binary string to an integer
    n = n - 1      # Subtract 1 from the integer
    return bin(n)[2:]  # Convert the result back to a binary string and return it