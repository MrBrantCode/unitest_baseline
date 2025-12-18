"""
QUESTION:
You can perform the following operations on the string, $a$:  

Capitalize zero or more of $a$'s lowercase letters.
Delete all of the remaining lowercase letters in $a$.

Given two strings, $a$ and $\boldsymbol{b}$, determine if it's possible to make $a$ equal to $\boldsymbol{b}$ as described. If so, print YES on a new line.  Otherwise, print NO.

For example, given $a=\textbf{AbcDE}$ and $b=\textbf{ABDE}$, in $a$ we can convert $\mbox{b}$ and delete $\textbf{C}$ to match $\boldsymbol{b}$.  If $a=\textbf{AbcDE}$ and $b=\textbf{AFDE}$, matching is not possible because letters may only be capitalized or discarded, not changed.

Function Description

Complete the function $abbreviation$ in the editor below.  It must return either $YES$ or $\mathrm{NO}$.

abbreviation has the following parameter(s):

a: the string to modify  
b: the string to match  

Input Format

The first line contains a single integer $\textit{q}$, the number of queries. 

Each of the next $\textit{q}$ pairs of lines is as follows: 

- The first line of each query contains a single string, $a$. 

- The second line of each query contains a single string, $\boldsymbol{b}$.  

Constraints

$1\leq q\leq10$  
$1\le|a|,|b|\le1000$
String $a$ consists only of uppercase and lowercase English letters, ascii[A-Za-z].
String $\boldsymbol{b}$ consists only of uppercase English letters, ascii[A-Z].

Output Format

For each query, print YES on a new line if it's possible to make string $a$ equal to string $\boldsymbol{b}$.  Otherwise, print NO.

Sample Input
1
daBcd
ABC

Sample Output
YES

Explanation

We have $\boldsymbol{a}=$ daBcd and $b=$ ABC. We perform the following operation:

Capitalize the letters a and c in $\boldsymbol{\alpha}$ so that $\boldsymbol{a}=$ dABCd. 
Delete all the remaining lowercase letters in $a$ so that $\boldsymbol{a}=$ ABC. 

Because we were able to successfully convert $a$ to $\boldsymbol{b}$, we print YES on a new line.
"""

def can_transform_to_abbreviation(a: str, b: str) -> str:
    # Check if b is a subsequence of the uppercase version of a
    def is_subseq(x, y):
        it = iter(y)
        return all(c in it for c in x)
    
    # Convert a to uppercase
    upper_a = a.upper()
    
    # Check if b is a subsequence of upper_a
    if not is_subseq(b, upper_a):
        return "NO"
    
    # Collect all uppercase letters in a
    must_include = [c for c in a if c.isupper()]
    
    # Check if all must_include letters are in b
    if not is_subseq(must_include, b):
        return "NO"
    
    # Count occurrences of each character in a and b
    count_a = Counter(upper_a)
    count_b = Counter(b)
    
    # Check if count_b can be satisfied by count_a
    if count_b - count_a:
        return "NO"
    
    return "YES"