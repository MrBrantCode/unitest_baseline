"""
QUESTION:
A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string.  Letters cannot be rearranged.  Given two strings of equal length, what's the longest string  that can be constructed such that it is a child of both?  

Example   

$\boldsymbol{s1=\text{'ABCD'}}$ 

$s2=\text{'ABDC'}$   

These strings have two children with maximum length 3, ABC and ABD.  They can be formed by eliminating either the D or C from both strings.  Return $3$.  

Function Description

Complete the commonChild function in the editor below.  

commonChild has the following parameter(s):

string s1:  a string
string s2:  another string   

Returns   

int: the length of the longest string which is a common child of the input strings 

Input Format

There are two lines, each with a string, $\mbox{sI}$ and $\mbox{s2}$. 

Constraints

$1\leq|s1|,\:|s2|\leq5000$ where $\left|s\right|$ means "the length of $\boldsymbol{\mathrm{~S~}}$"     
All characters are upper case in the range ascii[A-Z].

Sample Input
HARRY
SALLY

Sample Output
 2

Explanation

The longest string that can be formed by deleting zero or more characters from $\textit{HARRY}$ and $\textit{SALLY}$ is $\mbox{AY}$, whose length is 2.

Sample Input 1

AA
BB

Sample Output 1

0

Explanation 1

$\boldsymbol{AA}$ and $\textit{BB}$ have no characters in common and hence the output is 0.

Sample Input 2

SHINCHAN
NOHARAAA

Sample Output 2

3

Explanation 2

The longest string that can be formed between $\textit{SHINCHAN}$ and $\textit{NOHARAAA}$ while maintaining the order is $NHA$.

Sample Input 3

ABCDEF
FBDAMN

Sample Output 3

2

Explanation 3 

$\textit{BD}$ is the longest child of the given strings.
"""

def commonChild(s1, s2):
    # Initialize a 2D list to store lengths of longest common subsequence
    lengths = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    
    # Fill the lengths table
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])
    
    # The length of the longest common subsequence is found at the bottom-right corner of the table
    return lengths[len(s1)][len(s2)]