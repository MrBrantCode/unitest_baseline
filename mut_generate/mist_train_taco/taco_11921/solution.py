"""
QUESTION:
Given a String S consisting only lowercase alphabets and an integer K. Find the count of all substrings of length K which have exactly K-1 distinct characters. 
 
Example 1:
Input:
S = "abcc"
K = 2
Output:
1
Explanation:
Possible substrings of length K = 2 are
ab : 2 distinct characters
bc : 2 distinct characters
cc : 1 distinct character
Only one valid substring exists {"cc"}. 
Example 2:
Input:
S = "aabab"
K = 3
Output :
3
Explanation:
Possible substrings of length K = 3 are
aab : 2 distinct characters
aba : 2 distinct characters
bab : 2 distinct characters.
All of these Substrings are a possible answer,
so the count is 3.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countOfSubstrings() which takes a String S and an integer K as input and returns the count of substrings of length K having K-1 distinct characters.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(constant)
Constraints:
1 ≤ K ≤ |S| ≤ 10^{5}
"""

def count_substrings_with_k_minus_1_distinct_chars(s: str, k: int) -> int:
    count = 0
    dic = {}
    i = 0
    j = 0
    
    while j < len(s):
        if s[j] in dic:
            dic[s[j]] += 1
        else:
            dic[s[j]] = 1
        
        if j - i + 1 == k:
            if len(dic) == k - 1:
                count += 1
        
        elif j - i + 1 > k:
            dic[s[i]] -= 1
            if dic[s[i]] == 0:
                del dic[s[i]]
            i += 1
            if len(dic) == k - 1:
                count += 1
        
        j += 1
    
    return count