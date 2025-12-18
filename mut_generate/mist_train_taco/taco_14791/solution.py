"""
QUESTION:
Given two strings text and pattern, find the first index where pattern exactly matches with any substring of text.  
Return -1 if pattern doesn't exist as a substring in text.
Example 1:
Input:
text = gffgfg
pattern = gfg
Output: 3
Explanation:  Considering 0-based indexing, substring of text from 3rd to last index is gfg.
Example 2:
Input:
text = gffggg
pattern = gfg
Output: -1
Explanation: pattern "gfg" does not exist in the text.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMatching() which takes the strings text and pattern as the input parameters and returns the first index of matching.
Expected Time Complexity: O(|text| * |pattern|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |text|, |pattern| ≤  10^{3}
"""

def find_first_match_index(text: str, pattern: str) -> int:
    """
    Finds the first index where the pattern exactly matches with any substring of the text.
    
    Parameters:
    - text (str): The main text string.
    - pattern (str): The pattern string to be matched.
    
    Returns:
    - int: The first index of the matching substring. Returns -1 if the pattern does not exist in the text.
    """
    if pattern in text:
        return text.find(pattern)
    else:
        return -1