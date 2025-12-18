"""
QUESTION:
Given a pair of strings, Geek wants to find the better string. The better string is the string having more number of distinct subsequences.
If both the strings have equal count of distinct subsequence then return str1.
Example 1:
Input:
str1 = "gfg", str2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 7 distinct subsequences whereas "ggg" have 4 distinct subsequences. 
Example 2:
Input: str1 = "a", str2 = "b"
Output: "a"
Explanation: Both the strings have only 1 distinct subsequence. 
Constraints:
1 <= str1.lenght , str2.length <= 30
Your Task:
You don't need to read input or print anything. Your task is to complete the function betterString() which takes str1 and str2 as input parameters and returns the better string.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
"""

def better_string(str1, str2):
    def count_distinct_subsequences(s):
        count = 1
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = count
                count *= 2
            else:
                temp = dic[char]
                dic[char] = count
                count *= 2
                count -= temp
        return count
    
    cnt1 = count_distinct_subsequences(str1)
    cnt2 = count_distinct_subsequences(str2)
    
    if cnt1 >= cnt2:
        return str1
    return str2