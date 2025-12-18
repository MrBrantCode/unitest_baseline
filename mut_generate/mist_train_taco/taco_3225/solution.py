"""
QUESTION:
There are two kinds of bots A and B in a 1-D array. A bot can only move left while B can only move right. There are also empty spaces in between represented by #. But its also given that the bots cannot cross over each other. 
Given the initial state and final state, we should tell if the transformation is possible.
NOTE: There can be many bots of the same type in a particular array. 
Example 1:
Input:
s1 = #B#A#
s2 = ##BA#
Output: Yes
Explanation: Because we can reach the 
final state by moving 'B' to the 
right one step.
Example 2:
Input:
s1 = #B#A#
s2 = #A#B# 
Output: No
Explanation: Because the robots 
cannot cross each other.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function moveRobots() which takes the initial and final states as strings s1 and s2 respectively and returns if a valid transformation can be done. Return "Yes" if possible, else "No".
 
Expected Time Complexity: O(|s1|)
Expected Auxiliary Space: O(|s1|)
 
Constraints:
1 <= |s1| = |s2| <= 10^{5}
The strings only consists of 'A', 'B' and '#'.
"""

def can_transform(s1: str, s2: str) -> str:
    n1 = len(s1)
    n2 = len(s2)
    
    if n1 != n2:
        return 'No'
    
    i, j = 0, 0
    
    while i < n1 and j < n2:
        # Skip all '#' in s1
        while i < n1 and s1[i] == '#':
            i += 1
        # Skip all '#' in s2
        while j < n2 and s2[j] == '#':
            j += 1
        
        # If both strings are exhausted
        if i == n1 and j == n2:
            return 'Yes'
        
        # If one string is exhausted but not the other
        if i == n1 or j == n2:
            return 'No'
        
        # Check for invalid transformations
        if s1[i] == 'A' and s2[j] == 'B':
            return 'No'
        elif s1[i] == 'B' and s2[j] == 'A':
            return 'No'
        elif s1[i] == 'A' and i < j:
            return 'No'
        elif s1[i] == 'B' and i > j:
            return 'No'
        
        # Move to the next character
        i += 1
        j += 1
    
    return 'Yes'