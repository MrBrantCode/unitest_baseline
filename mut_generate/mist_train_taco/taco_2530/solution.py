"""
QUESTION:
Consider the following:

A string, $\boldsymbol{\mathrm{~S~}}$, of length $n$ where $s=c_0c_1\ldots c_{n-1}$.
An integer, $\boldsymbol{\mbox{k}}$, where $\boldsymbol{\mbox{k}}$ is a factor of $n$.

We can split $\boldsymbol{\mathrm{~S~}}$ into $\frac{n}{k}$ substrings where each subtring, $t_i$, consists of a contiguous block of $\boldsymbol{\mbox{k}}$ characters in $\boldsymbol{\mathrm{~S~}}$. Then, use each $t_i$ to create string $u_i$ such that:

The characters in $u_i$ are a subsequence of the characters in $t_i$. 
Any repeat occurrence of a character is removed from the string such that each character in $u_i$ occurs exactly once. In other words, if the character at some index $j$ in $t_i$ occurs at a previous index $\lt j$ in $t_i$, then do not include the character in string $u_i$.

Given $\boldsymbol{\mathrm{~S~}}$ and $\boldsymbol{\mbox{k}}$, print $\frac{n}{k}$ lines where each line $\boldsymbol{i}$ denotes string $u_i$.  

Example 

$s=\text{'AAABCADDE'}$ 

$k=3$  

There are three substrings of length $3$ to consider: 'AAA', 'BCA' and 'DDE'.  The first substring is all 'A' characters, so $u_1=\text{'A'}$.  The second substring has all distinct characters, so $u_2=\text{'BCA'}$.  The third substring has $2$ different characters, so $u_3=\text{'DE'}$.  Note that a subsequence maintains the original order of characters encountered.  The order of characters in each subsequence shown is important.  

Function Description  

Complete the merge_the_tools function in the editor below.  

merge_the_tools has the following parameters:  

string s: the string to analyze  
int k: the size of substrings to analyze  

Prints  

Print each subsequence on a new line.  There will be $\frac{n}{k}$ of them.  No return value is expected.  

Input Format

The first line contains a single string, $\boldsymbol{\mathrm{~S~}}$. 

The second line contains an integer, $\boldsymbol{\mbox{k}}$, the length of each substring.

Constraints

$1\leq n\leq10^4$, where $n$ is the length of $\boldsymbol{\mathrm{~S~}}$
$1\leq k\leq n$ 
It is guaranteed that $n$ is a multiple of $\boldsymbol{\mbox{k}}$. 

Sample Input
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output
AB
CA
AD

Explanation

Split $\boldsymbol{\mathrm{~S~}}$ into $\frac{n}{k}=\frac{9}{3}=3$ equal parts of length $k=3$. Convert each $t_i$ to $u_i$ by removing any subsequent occurrences of non-distinct characters in $t_i$:

$t_0=\textsf{"AAB"}\to u_0=\textsf{"AB"}$
$t_1=\text{"CAA}\rightarrow u_1=\text{"CA}\text{"}$
$t_2=\text{"ADA}\text{"}\rightarrow u_2=\text{"AD}\text{"}$

Print each $u_i$ on a new line.
"""

def generate_unique_subsequences(s: str, k: int) -> list[str]:
    n = len(s)
    result = []
    
    for i in range(0, n, k):
        substring = s[i:i+k]
        unique_chars = []
        seen = set()
        
        for char in substring:
            if char not in seen:
                unique_chars.append(char)
                seen.add(char)
        
        result.append(''.join(unique_chars))
    
    return result