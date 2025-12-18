"""
QUESTION:
Given strings str1 and str2, find the minimum (contiguous) substring W of str1, so that str2 is a subsequence of W.
If there is no such window in str1 that covers all characters in str2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
 
Example 1:
Input: 
str1: geeksforgeeks
str2: eksrg
Output: 
eksforg
Explanation: 
Eksforg satisfies all required conditions. str2 is its subsequence and it is longest and leftmost among all possible valid substrings of str1.
Example 2:
Input: 
str1: abcdebdde
str2: bde
Output: 
bcde
Explanation: 
"bcde" is the answer and "deb" is not a smaller window because the elements of T in the window must occur in order.
Your Task:
Complete the function string minWindow(string str1, string str2), which takes two strings as input and returns the required valid string as output.
Expected Time Complexity: O(N^{2}).
Expected Auxiliary Space: O(N^{2}).
Constraints:
0 <= str1 <= 1000
0 <= str2 <= 100
"""

def find_min_window(str1, str2):
    if not str1 or not str2:
        return ''
    
    n, m = len(str1), len(str2)
    ans = ''
    
    for i in range(n):
        if str1[i] != str2[0]:
            continue
        
        j, k = i + 1, 1
        while j < n and k < m:
            if str1[j] == str2[k]:
                j += 1
                k += 1
            else:
                j += 1
        
        if k == m:
            if not ans or j - i < len(ans):
                ans = str1[i:j]
    
    return ans