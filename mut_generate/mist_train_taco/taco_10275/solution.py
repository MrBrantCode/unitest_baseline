"""
QUESTION:
Given a string S of length N, find the pattern of the strings as shown below in the examples.
Example 1:
Input: S = "GeeK"
Output: Geek
        Gee
        Ge
        G
Explanation: Decrease one character 
after each line
Ã¢â¬â¹Example 2:
Input: S = "G*g" 
Output: G*g
        G*
        G
Explanation: Decrease one character
after each line
Your Task:  
You don't need to read input or print anything. Your task is to complete the function pattern() which takes the string S as inputs and returns the answer as a list of strings.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 ≤ N ≤ 10^{3}
"""

def generate_pattern(S: str) -> list[str]:
    """
    Generates a pattern of strings by decreasing one character after each line.

    Parameters:
    S (str): The input string of length N (1 ≤ N ≤ 10^3).

    Returns:
    list[str]: A list of strings where each string represents a line in the pattern.
    """
    pattern_list = []
    for i in range(len(S), 0, -1):
        pattern_list.append(S[:i])
    return pattern_list