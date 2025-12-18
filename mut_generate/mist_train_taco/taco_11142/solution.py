"""
QUESTION:
Archana is very fond of strings.  Help her to solve a problem. The problem is as follows:-
Given is a string of length L. Her task is to find the longest string from the given string with characters arranged in descending order of their ASCII code and in arithmetic progression. She wants the common difference should be as low as possible(at least 1) and the characters of the string to be of higher ASCII value. 
Example 1:
Input:
s = "ABCPQR"
Output: "RQP"
Explanation: Two strings of maximum length
             are possible- “CBA” and “RPQ”.
             But he wants the string to be 
             of higher ASCII value 
             therefore, the output is “RPQ”.
Example 2:
Input:
s = "ADGJPRT"
Output: "JGDA"
Explanation: The String of maximum length
             is “JGDA”.
User Task:
Your task is to complete the function findString() which takes a single argument(string s) and returns the answer. You need not take any input or print anything.
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(number of distinct alphabets)
Constraints:
3 <= L <= 1000
A <= s[i] <= Z
The string contains minimum three different characters.
"""

def find_longest_desc_arithmetic_string(s: str) -> str:
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('A')] += 1
    
    a = ['#'] * 26
    for i in range(26):
        if cnt[i] > 0:
            a[i] = chr(ord('A') + i)
    
    ans = ''
    diff = 2000
    
    for i in range(25, -1, -1):
        if a[i] == '#':
            continue
        for j in range(1, 26):
            c = ''
            for k in range(i, -1, -j):
                if a[k] == '#':
                    break
                c += a[k]
            if len(c) > len(ans) or (len(c) == len(ans) and diff > j):
                ans = c
                diff = j
    
    return ans