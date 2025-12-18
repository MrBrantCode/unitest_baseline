"""
QUESTION:
Two words are anagrams of one another if their letters can be rearranged to form the other word.  

Given a string, split it into two contiguous substrings of equal length.  Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

Example 

$s=\textbf{abccde}$  

Break $\boldsymbol{\mathrm{~S~}}$ into two parts: 'abc' and 'cde'.  Note that all letters have been used, the substrings are contiguous and their lengths are equal.  Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams.  Two changes were necessary.

Function Description

Complete the anagram function in the editor below.    

anagram has the following parameter(s):  

string s: a string  

Returns  

int: the minimum number of characters to change or -1. 

Input Format

The first line will contain an integer, $\textit{q}$, the number of test cases. 

Each test case will contain a string $\boldsymbol{\mathrm{~S~}}$.

Constraints

$1\leq q\leq100$ 

$1\leq|s|\leq10^4$  
$\boldsymbol{\mathrm{~S~}}$ consists only of characters in the range ascii[a-z].  

Sample Input
6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx

Sample Output
3
1
-1
2
0
1

Explanation

Test Case #01: We split $\boldsymbol{\mathrm{~S~}}$ into two strings $\mbox{S1}$='aaa' and $\mbox{S2}$='bbb'.  We have to replace all three characters from the first string with 'b' to make the strings anagrams. 

Test Case #02: You have to replace 'a' with 'b', which will  generate "bb". 

Test Case #03: It is not possible for two strings of unequal length to be anagrams of one another. 

Test Case #04: We have to replace both the characters of first string ("mn") to make it an anagram of the other one. 

Test Case #05: $\mbox{S1}$ and $\mbox{S2}$ are already anagrams of one another. 

Test Case #06: Here S1 = "xaxb" and S2 = "bbxx". You must replace 'a' from S1 with 'b' so that S1 = "xbxb".
"""

def min_changes_to_anagram(s: str) -> int:
    l = len(s)
    
    # If the length of the string is odd, it's not possible to split into two equal parts
    if l % 2 != 0:
        return -1
    
    half = l // 2
    a = s[:half]
    b = s[half:]
    
    # Count the frequency of each character in both substrings
    from collections import Counter
    count_a = Counter(a)
    count_b = Counter(b)
    
    # Calculate the number of changes needed
    changes = 0
    for char in count_a:
        if count_a[char] > count_b.get(char, 0):
            changes += count_a[char] - count_b.get(char, 0)
    
    return changes