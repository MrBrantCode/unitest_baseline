"""
QUESTION:
Shubham recently learned the lexicographical order in strings.

Now, he has two strings s1  and  s2  of the equal size and Shubham wants to compare those two strings lexicographically.

Help Shubham with the strings comparison.

Note:

Letters are case insensitive. 


-----Input-----

First line contains a integer T denoting the number of test cases. Each test case contains two strings of equal size in two separate lines.

-----Output-----

For each test case,

If s1 < s2, print "first".

If s1 > s2, print "second".

If s1=s2, print "equal".


in separate lines.

-----Constraints-----

- 1 ≤ T ≤ 10^2
- 1 ≤ Length of the string ≤ 500

-----Example-----
Input:
2
abc
acb
AB
ba

Output:
first
first
"""

def compare_lexicographically(s1: str, s2: str) -> str:
    # Convert both strings to lowercase
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Compare the strings character by character
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            return "first"
        elif s1[i] > s2[i]:
            return "second"
    
    # If all characters are equal, the strings are equal
    return "equal"