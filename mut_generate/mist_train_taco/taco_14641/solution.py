"""
QUESTION:
Given a string S. The task is to count the number of substrings which contains equal number of lowercase and uppercase letters. 
Example 1:
Input:
S = "gEEk"
Output: 3
Explanation: There are 3 substrings of
the given string which satisfy the
condition. They are "gE", "gEEk" and "Ek".
Example 2:
Input:
S = "WomensDAY"
Output: 4
Explanation: There are 4 substrings of 
the given string which satisfy the
condition. They are "Wo", "ensDAY", 
"nsDA" and "sD"
Your Task:
The task is to complete the function countSubstring() which takes the string S as input parameter and returns the number of substrings which contains equal number of uppercase and lowercase letters.
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{3}
"""

def count_equal_case_substrings(S: str) -> int:
    count = 0
    for i in range(len(S)):
        upper = 0
        lower = 0
        if S[i].isupper():
            upper += 1
        else:
            lower += 1
        for j in range(i + 1, len(S)):
            if S[j].isupper():
                upper += 1
            else:
                lower += 1
            if upper == lower:
                count += 1
    return count