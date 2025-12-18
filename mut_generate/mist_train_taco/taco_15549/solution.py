"""
QUESTION:
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.  

Example 

$s=mom$  

The list of all anagrammatic pairs is $[m,m],[mo,om]$ at positions $[[0],[2]],[[0,1],[1,2]]$ respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below.  

sherlockAndAnagrams has the following parameter(s):

string s: a string  

Returns  

int: the number of unordered anagrammatic pairs of substrings in $\boldsymbol{\mathrm{~S~}}$

Input Format

The first line contains an integer $\textit{q}$, the number of queries. 

Each of the next $\textit{q}$ lines contains a string $s$ to analyze. 

Constraints

$1\leq q\leq10$ 

$2\leq length of s\leq100$ 

$s$ contains only lowercase letters in the range ascii[a-z]. 

Sample Input 0
2
abba
abcd

Sample Output 0
4
0

Explanation 0

The list of all anagrammatic pairs is $[a,a],[ab,ba],[b,b]$ and $[abb,bba]$ at positions $[[0],[3]],[[0,1],[2,3]],[[1],[2]]$ and $[[0,1,2],[1,2,3]]$ respectively.  

No anagrammatic pairs exist in the second query as no character repeats.

Sample Input 1
2
ifailuhkqq
kkkk

Sample Output 1
3
10

Explanation 1

For the first query, we have anagram pairs $[i,i],[q,q]$ and $[if a,fai]$ at positions $[[0],[3]],[[8],[9]]$ and $[[0,1,2],[1,2,3]]$ respectively.

For the second query: 

There are 6 anagrams of the form $[k,k]$ at positions $[[0],[1]],[[0],[2]],[[0],[3]],[[1],[2]],[[1],[3]]$ and $[[2],[3]]$. 

There are 3 anagrams of the form $[kk,kk]$ at positions $[[0,1],[1,2]],[[0,1],[2,3]]$ and $[[1,2],[2,3]]$. 

There is 1 anagram of the form $[kkk,kkk]$ at position $[[0,1,2],[1,2,3]]$.

Sample Input 2
1
cdcd

Sample Output 2
5

Explanation 2

There are two anagrammatic pairs of length $1$: $[c,c]$ and $[d,d]$. 

There are three anagrammatic pairs of length $2$: $[cd,dc],[cd,cd],[dc,cd]$ at positions $[[0,1],[1,2]],[[0,1],[2,3]],[[1,2],[2,3]]$ respectively.
"""

def sherlock_and_anagrams(s: str) -> int:
    from collections import defaultdict
    
    # Dictionary to store the frequency of each sorted substring
    was = defaultdict(int)
    
    # Length of the input string
    n = len(s)
    
    # Generate all substrings and count their sorted versions
    for i in range(n):
        for j in range(i, n):
            cur = s[i:j + 1]
            cur = ''.join(sorted(cur))
            was[cur] += 1
    
    # Calculate the number of anagrammatic pairs
    ans = 0
    for v in was.values():
        ans += v * (v - 1) // 2
    
    return ans