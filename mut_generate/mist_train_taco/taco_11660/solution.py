"""
QUESTION:
Given two strings X and Y, the task is to find the last index in X at which string Y appears, if Y does not appear then the answer is -1. 
Example 1:
Input: X = "geeksforgeeks", Y = "geeks"
output: 9
Explanation: string "geeks" appears at 
index 1 and 9
Example 2:
Input: X = "geesforgees", Y = "geeks" 
output: -1 
Explanation: "geeks" does not appear
Your task:
You do not need to read any input or print anything. The task is to complete the function search(), which takes two strings as input and returns an integer. 
Expected Time Complexity: O(|X| + |Y|)
Expected Auxiliary Space: O(|X| + |Y|)
Constraints:
1 ≤ |X|, |Y| ≤ 10^{5}
Both the strings contains lower case English alphabets
"""

def find_last_index(X: str, Y: str) -> int:
    """
    Finds the last index of the substring Y in the string X.
    
    Parameters:
    X (str): The main string in which to search.
    Y (str): The substring to find the last index of in X.
    
    Returns:
    int: The last index of Y in X, or -1 if Y is not found in X.
    """
    if Y not in X:
        return -1
    else:
        return X.rfind(Y)