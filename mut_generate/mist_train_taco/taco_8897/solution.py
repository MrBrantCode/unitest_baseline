"""
QUESTION:
Given a string S, remove all the characters other than the alphabets.
Example 1:
Input: S = "$Gee*k;s..fo, r'Ge^eks?"
Output: GeeksforGeeks
Explanation: Removed charcters other than
alphabets. 
 
Example 2:
Input:  S = "{{{}}> *& ^%*)"
Output: -1
Explanation: There are no alphabets.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function removeSpecialCharacter() which takes string S as input parameter and returns the resultant string. Return "-1" if no alphabets remain.
 
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)
 
Constraints:
1 <= |S| <= 10^{5}
"""

def remove_special_characters(S: str) -> str:
    """
    Removes all special characters from the input string and returns the resultant string.
    If no alphabets remain after removal, returns "-1".

    Parameters:
    S (str): The input string.

    Returns:
    str: The resultant string after removing special characters or "-1" if no alphabets remain.
    """
    result = ''.join(char for char in S if char.isalpha())
    return result if result else "-1"