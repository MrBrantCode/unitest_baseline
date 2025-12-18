"""
QUESTION:
Given a string s, find lexicographically previous permutation of it.
For example: Lexicographically previous permutation of “4321” is “4312". If the string is sorted in ascending order, then the lexicographically previous permutation doesn’t exist.
Example 1:
Input: s = "4321"
Output: "4312" 
Explanation: lexicographically previous
permutation of “4321” is “4312”
Example 2:
Input: s = "1234"
Output: "None"
Explanation: "1234" is sorted in
ascending order, hence "None". 
Your Task:  
You dont need to read input or print anything. Complete the function prevPermutation() which takes string s as input parameter and returns lexicographically previous permutation of s and if there is no lexicographically previous permutation of s, it returns "None".
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |s| ≤ 10^{3}
"""

def prev_permutation(s: str) -> str:
    # Convert the string to a list of integers
    s = [int(i) for i in s]
    
    # Find the inversion point
    inversion_point = len(s) - 2
    while inversion_point >= 0 and s[inversion_point] <= s[inversion_point + 1]:
        inversion_point -= 1
    
    # If no inversion point is found, return "None"
    if inversion_point == -1:
        return "None"
    
    # Find the largest index i such that s[i] < s[inversion_point]
    for i in reversed(range(inversion_point + 1, len(s))):
        if s[i] < s[inversion_point]:
            # Swap the elements at inversion_point and i
            (s[inversion_point], s[i]) = (s[i], s[inversion_point])
            break
    
    # Reverse the suffix starting from inversion_point + 1
    s[inversion_point + 1:] = s[:inversion_point:-1]
    
    # Convert the list back to a string
    s = [str(i) for i in s]
    return ''.join(s)