"""
QUESTION:
Remove all characters except the numeric characters from an alphanumeric string.
Example 1:
Input: S = "AA1d23cBB4"
Output: 1234
Explanation: Remove all characters
other than numbers
Example 2:
Input: S = "a1b2c3"
Output: 123
Explanation: Remove all characters
other than numbers
Your task:
Your task is to complete the function string() which takes a single string as input and returns the string. You need not take any input or print anything.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 <= |S| <= 10^{5}
"""

def extract_numeric_characters(S: str) -> str:
    """
    Extracts and returns only the numeric characters from the input string.

    Parameters:
    S (str): The input alphanumeric string.

    Returns:
    str: A string containing only the numeric characters from the input string.
    """
    result = ''
    for char in S:
        if char.isdigit():
            result += char
    return result