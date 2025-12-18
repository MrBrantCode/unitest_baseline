"""
QUESTION:
Given two strings  S1 and S2 . You have to concatenate both the strings and print the concatenated string.
Example 1:
Input:
S1 = "Geeksfor"
S2 = "Geeks"
Output: GeeksforGeeks
Explanation: Combined "Geeksfor" and "Geeks"
 
Example 2:
Input:
S1 = "Practice"
S2 = "Hard"
Output: PracticeHard
Explanation: Combined "Practice" and "Hard"
 
Your Task:  
You dont need to read input or print anything. Complete the function conCat() which accepts two strings S1 and S2 as input parameter and returns concatenated string.
Expected Time Complexity: O(|S1| + |S2|) .
Expected Auxiliary Space: O(|S1| + |S2|) .
where N is the length of a String
Constraints:
1 <= |S1| , |S2| <= 10^{5}
|S| denotes the length of the string S.
"""

def concatenate_strings(s1: str, s2: str) -> str:
    """
    Concatenates two strings s1 and s2.

    Parameters:
    s1 (str): The first string to be concatenated.
    s2 (str): The second string to be concatenated.

    Returns:
    str: The concatenated string of s1 and s2.
    """
    return s1 + s2