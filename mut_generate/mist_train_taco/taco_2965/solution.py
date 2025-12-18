"""
QUESTION:
Find the longest subsequence X of a string A which is a substring Y of a string B.
Note: All letters of the Strings are Uppercased.
 
Example 1: 
Input:
A = "ABCD" , B = "BACDBDCD"
Output:
3
Explanation:
The answer would be 3 as because "ACD"
is the longest subsequence of A which
is also a substring of B.
Example 2:
Input:
A = "A" , B = "A"
Output:
1
Explanation:
The answer would be 1 as because "A"
is the longest subsequence of A which
is also a substring of B. 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getLongestSubsequence() which takes Strings A  and B as input and returns the answer.
 
Expected Time Complexity: O(|S|^{2})
Expected Auxiliary Space: O(|S|^{2})
 
Constraints:
1 <= |A|,|B| <= 10^{3}
"""

def get_longest_subsequence(A: str, B: str) -> int:
    na, nb = len(A), len(B)
    ans = 0
    
    for i in range(nb):
        k = i
        temp = 0
        for j in range(na):
            if k < nb and A[j] == B[k]:
                k += 1
                temp += 1
        ans = max(ans, temp)
    
    return ans