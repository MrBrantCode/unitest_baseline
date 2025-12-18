"""
QUESTION:
Given a number in its binary form find if the given binary number is a multiple of 3. It is recommended to finish the task using one traversal of input binary number.
Example 1:
Input: S = "0011"
Output: 1
Explanation: "0011" is 3, which is divisible by 3.
Example 2:
Input: S = "100"
Output: 0
Explanation: "100"'s decimal equivalent is 4, which is not divisible by 3.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isDivisible() which takes the string s as inputs and returns 1 if the given number is divisible by 3 otherwise 0.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{5}
"""

def is_divisible_by_three(s: str) -> int:
    """
    Determines if the given binary number represented by the string s is divisible by 3.

    Parameters:
    s (str): The binary number as a string.

    Returns:
    int: 1 if the binary number is divisible by 3, otherwise 0.
    """
    n = int(s, 2)
    if n % 3 == 0:
        return 1
    return 0