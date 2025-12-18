"""
QUESTION:
Given a string consisting of lowercase letters, arrange all its letters in ascending order. 
Example 1:
Input:
S = "edcab"
Output: "abcde"
Explanation: characters are in ascending
order in "abcde".
Example 2:
Input:
S = "xzy"
Output: "xyz"
Explanation: characters are in ascending
order in "xyz".
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sort() which takes the string as inputs and returns the modified string.
Expected Time Complexity: O(|S| * log |S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{5}
S contains only lowercase alphabets.
"""

def sort_string(s: str) -> str:
    """
    Sorts the characters of the input string in ascending order.

    Parameters:
    s (str): The input string consisting of lowercase letters.

    Returns:
    str: The sorted string with characters in ascending order.
    """
    return ''.join(sorted(s))