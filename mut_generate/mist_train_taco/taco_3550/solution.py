"""
QUESTION:
Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.
Example 1:
Input:
S = "01212"
Output:
3
Explanation:
The substring 012 is the smallest substring
that contains the characters 0, 1 and 2.
Example 2:
Input: 
S = "12121"
Output:
-1
Explanation: 
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.
Your Task:
Complete the function smallestSubstring() which takes the string S as input, and returns the length of the smallest substring of string S that contains all the three characters 0, 1 and 2.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{5}
All the characters of String S lies in the set {'0', '1', '2'}
"""

def find_smallest_substring_length(S: str) -> int:
    c = 99999
    x = 0
    y = 0
    o = 0
    z = 0
    t = 0
    
    for i in range(len(S)):
        if S[i] == '0':
            z += 1
        if S[i] == '1':
            o += 1
        if S[i] == '2':
            t += 1
        y += 1
        
        while o > 0 and z > 0 and t > 0:
            if S[x] == '0':
                z -= 1
            if S[x] == '1':
                o -= 1
            if S[x] == '2':
                t -= 1
            if c > y - x:
                c = y - x
            x += 1
    
    if c != 99999:
        return c
    else:
        return -1