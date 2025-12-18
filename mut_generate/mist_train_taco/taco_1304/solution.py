"""
QUESTION:
Given a string s consisting of uppercase and lowercase alphabetic characters. Return the  number of distinct substrings of size 2 that appear in s as contiguous substrings.
Example
Input :
s = "ABCAB"
Output :
3
Explanation:  For "ABCAB", the 
three distinct substrings of size 
2 are "AB", "BC" and "CA". 
Example
Input :
s = "XYZ"
Output :
2
Explanation: For "XYZ", the 
two distinct substrings of size 2 are
"XY" and "YZ".
Your Task :
You don't need to read input or print anything. You have to complete the function fun() which takes the string s as input parameter and returns the number of distinct contiguous substring of size 2.
Expected Time Complexity : O(|s|)
Expected Auxilliary Space : O(|s|)
Constraints:
1<=|s|<=100
|s| denotes the length of the string s.
"""

def count_distinct_substrings(s: str) -> int:
    d = {}
    for i in range(len(s) - 1):
        substring = (s[i], s[i + 1])
        if substring not in d:
            d[substring] = 1
        else:
            d[substring] += 1
    return len(d)