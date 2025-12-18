"""
QUESTION:
You are given a string containing characters $\mbox{A}$ and $\mbox{B}$ only.  Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.  

Your task is to find the minimum number of required deletions.

Example 

$\textbf{s}=\textit{AABAAB}$  

Remove an $\mbox{A}$ at positions $0$ and $3$ to make $\textbf{s}=\textit{ABAB}$ in $2$ deletions.

Function Description

Complete the alternatingCharacters function in the editor below.  

alternatingCharacters has the following parameter(s):

string s: a string  

Returns  

int: the minimum number of deletions required

Input Format

The first line contains an integer $\textit{q}$, the number of queries. 

The next $\textit{q}$ lines each contain a string $\boldsymbol{\mathrm{~S~}}$ to analyze.

Constraints

$1\leq q\leq10$  
$1\leq\:\text{length of s}\:\leq10^5$
Each string $\boldsymbol{\mathrm{~S~}}$ will consist only of characters $\mbox{A}$ and $\mbox{B}$.

Sample Input
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output
3
4
0
0
4

Explanation

The characters marked red are the ones that can be deleted so that the string does not have matching adjacent characters.
"""

def alternating_characters(s: str) -> int:
    """
    Calculate the minimum number of deletions required to ensure no two adjacent characters in the string are the same.

    Parameters:
    s (str): The input string containing only characters 'A' and 'B'.

    Returns:
    int: The minimum number of deletions required.
    """
    return sum(1 for c1, c2 in zip(s, s[1:]) if c1 == c2)