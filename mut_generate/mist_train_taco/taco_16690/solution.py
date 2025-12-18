"""
QUESTION:
In this problem, we'll use the term "longest common substring" loosely.  It refers to substrings differing at some number or fewer characters when compared index by index.  For example, 'abc' and 'adc' differ in one position, 'aab' and 'aba' differ in two.  

Given two strings and an integer $\boldsymbol{\mbox{k}}$, determine the length of the longest common substrings of the two strings that differ in no more than $\boldsymbol{\mbox{k}}$ positions.  

For example, $k=1$.  Strings $s1=abcd$ and $s2=bbca$.  Check to see if the whole string (the longest substrings) matches.  Given that neither the first nor last characters match and $2>k$, we need to try shorter substrings.  The next longest substrings are $s1'=[abc,bcd]$ and $s2'=[bbc,bca]$.  Two pairs of these substrings only differ in $\mbox{1}$ position: $[abc,bbc]$ and $[bcd,bca]$.  They are of length $3$.  

Function Description

Complete the substringDiff function in the editor below.  It should return an integer that represents the length of the longest common substring as defined.  

substringDiff has the following parameter(s):  

k: an integer that represents the maximum number of differing characters in a matching pair  
s1: the first string  
s2: the second string  

Input Format

The first line of input contains a single integer, $\boldsymbol{\boldsymbol{t}}$, the number of test cases follow. 

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains three space-separated values:  an integer $\boldsymbol{\mbox{k}}$ and two strings, $\mbox{sI}$ and $\mbox{s2}$.

Constraints

$1\leq t\leq10$  
$0\leq k\leq|s1|$   
$|s1|=|s2|$  
$1\leq|s1|,|s2|\leq1500$
All characters in $\mbox{s1}$ and $s2\in a s c i[a-z]$.

Output Format

For each test case, output a single integer which is the length of the maximum length common substrings differing at $\boldsymbol{\mbox{k}}$ or fewer positions.

Sample Input
3
2 tabriz torino
0 abacba abcaba
3 helloworld yellomarin

Sample Output
4
3
8

Explanation

First test case: If we take "briz" from the first string, and "orin" from the second string, then the number of mismatches between these two substrings is equal to 2 and their lengths are $4$.

Second test case: Since $k=0$, we should find the longest common substring, standard definition, for the given input strings. We choose "aba" as the result.

Third test case: We can choose "hellowor" from first string and "yellomar" from the second string.
"""

def longest_common_substring_diff(k: int, s1: str, s2: str) -> int:
    def l_func(p: str, q: str, max_s: int) -> int:
        n = len(q)
        res_ar = [0]
        count = 0
        ans = 0
        for i in range(n):
            if p[i] != q[i]:
                res_ar.append(i + 1)
                count += 1
                if count > max_s:
                    l = res_ar[-1] - res_ar[-2 - max_s] - 1
                    if l > ans:
                        ans = l
        if count <= max_s:
            return n
        return ans

    def check_func(p: str, q: str, s: int) -> int:
        n = len(q)
        ans = 0
        for i in range(n):
            if n - i <= ans:
                break
            l = l_func(p, q[i:], s)
            if l > ans:
                ans = l
        for i in range(n):
            if n - i <= ans:
                break
            l = l_func(q, p[i:], s)
            if l > ans:
                ans = l
        return ans

    return check_func(s1, s2, k)