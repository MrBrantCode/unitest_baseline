"""
QUESTION:
Given a binary string S. The task is to count the number of substrings that start and end with 1. For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.
Example 1:
Input:
N = 4
S = 1111
Output: 6
Explanation: There are 6 substrings from
the given string. They are 11, 11, 11,
111, 111, 1111.
Example 2:
Input:
N = 5
S = 01101
Output: 3
Explanation: There 3 substrings from the
given string. They are 11, 101, 1101.
Your Task:
The task is to complete the function binarySubstring() which takes the length of binary string n and a binary string a as input parameter and counts the number of substrings starting and ending with 1 and returns the count.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ |S| ≤ 10^{4}
"""

def count_substrings_starting_ending_with_1(s: str) -> int:
    """
    Counts the number of substrings in a binary string that start and end with '1'.

    Parameters:
    s (str): The binary string.

    Returns:
    int: The count of substrings that start and end with '1'.
    """
    # Count the number of '1's in the string
    no_1 = sum(1 for char in s if char == '1')
    
    # Calculate the number of valid substrings using the formula
    # (number of '1's) * (number of '1's - 1) // 2
    return no_1 * (no_1 - 1) // 2