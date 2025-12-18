"""
QUESTION:
Amanda has a string of lowercase letters that she wants to copy to a new string.  She can perform the following operations with the given costs. She can perform them any number of times to construct a new string $\boldsymbol{p}$:

Append a character to the end of string $\boldsymbol{p}$ at a cost of $\mbox{1}$ dollar. 
Choose any substring of $\boldsymbol{p}$ and append it to the end of $\boldsymbol{p}$ at no charge.

Given $n$ strings $s[i]$, find and print the minimum cost of copying each $s[i]$ to $p[i]$ on a new line.

For example, given a string $s=abcabc$, it can be copied for $3$ dollars.  Start by copying $\boldsymbol{a}$, $\boldsymbol{b}$ and $\textbf{c}$ individually at a cost of $\mbox{1}$ dollar per character.  String $p=abc$ at this time.  Copy $p[0:2]$ to the end of $\boldsymbol{p}$ at no cost to complete the copy.  

Function Description  

Complete the stringConstruction function in the editor below.  It should return the minimum cost of copying a string.  

stringConstruction has the following parameter(s):  

s: a string  

Input Format

The first line contains a single integer $n$, the number of strings. 

Each of the next $n$ lines contains a single string, $s[i]$.

Constraints

$1\leq n\leq5$  
$1\leq|s[i]|\leq10^5$  

Subtasks

$1\leq|s[i]|\leq10^3$ for $45\%$ of the maximum score.

Output Format

For each string $s[i]$ print the minimum cost of constructing a new string $p[i]$ on a new line.

Sample Input
2
abcd
abab

Sample Output
4
2

Explanation

Query 0: We start with $s=\text{"abcd''}$ and $p=\textsf{""}$.

Append character '$\mbox{a}$' to $\boldsymbol{p}$ at a cost of $\mbox{1}$ dollar, $p=\text{"a"}$. 
Append character '$\mbox{b}$' to $\boldsymbol{p}$ at a cost of $\mbox{1}$ dollar, $p=\text{"ab"}$. 
Append character '$\boldsymbol{\mathsf{c}}$' to $\boldsymbol{p}$ at a cost of $\mbox{1}$ dollar, $p=\text{"abc"}$. 
Append character '$\mbox{d}$' to $\boldsymbol{p}$ at a cost of $\mbox{1}$ dollar, $p=\text{"abcd"}$. 

Because the total cost of all operations is $1+1+1+1=4$ dollars, we print $4$ on a new line.

Query 1: We start with $s=\text{"abab''}$ and $p=\text{""}$.

Append character '$\mbox{a}$' to $\boldsymbol{p}$ at a cost of $\mbox{1}$ dollar, $p=\text{"a"}$. 
Append character '$\mbox{b}$' to $\boldsymbol{p}$ at a cost of $\mbox{1}$ dollar, $p=\text{"ab"}$. 
Append substring $\text{"ab''}$ to $\boldsymbol{p}$ at no cost, $p=\text{"abab''}$. 

Because the total cost of all operations is $1+1=2$ dollars, we print $2$ on a new line.

Note

A substring of a string $\mbox{S}$ is another string $S^{\prime}$ that occurs "in" $\mbox{S}$ (Wikipedia). For example, the substrings of the string "$\boldsymbol{abc}$" are "$\boldsymbol{a}$", "$\boldsymbol{b}$" ,"$\textbf{c}$", "$\boldsymbol{ab}$", "$\boldsymbol{bc}$", and "$\boldsymbol{abc}$".
"""

def calculate_min_copy_cost(s: str) -> int:
    """
    Calculate the minimum cost of copying the string `s` to a new string `p`.

    The cost is determined by the number of unique characters in the string `s`.
    Each unique character must be appended to `p` at a cost of 1 dollar.

    Parameters:
    s (str): The input string to be copied.

    Returns:
    int: The minimum cost of copying the string `s`.
    """
    return len(set(s))