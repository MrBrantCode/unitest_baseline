"""
QUESTION:
Given two strings consisting of lowercase english alphabets, the task is to check whether these strings are meta strings or not. Meta strings are the strings which can be made equal by exactly one swap in any of the strings. Equal string are not considered here as Meta strings.
Example 1:
Input:
S1 = "geeks", S2 = "keegs"
Output: 1
Explanation: We can swap the 0th and 3rd
character of S2 to make it equal to S1.
Ã¢â¬â¹Example 2:
Input: 
S1 = "geeks", S2 = "geeks"
Output: 0
Explanation: Equal strings are not considered
Meta strings.
Your Task:
You don't need to read input or print anything. Your task is to complete the function metaStrings() which takes the strings S1 and S2 as input and returns true if both the strings are meta strings, else it returns false.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
"""

def are_meta_strings(S1: str, S2: str) -> bool:
    # Check if the lengths of the strings are different
    if len(S1) != len(S2):
        return False
    
    # Find the positions where the characters differ
    diff_positions = []
    for i in range(len(S1)):
        if S1[i] != S2[i]:
            diff_positions.append(i)
    
    # Check if there are exactly two differences and they can be swapped
    if len(diff_positions) == 2:
        i, j = diff_positions
        if S1[i] == S2[j] and S1[j] == S2[i]:
            return True
    
    return False