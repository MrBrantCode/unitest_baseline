"""
QUESTION:
Given two strings, determine if they share a common substring.  A substring may be as small as one character.  

Example 

$s1=\text{'and'}$ 

$s2=\text{'art'}$  

These share the common substring $\class{ML__boldsymbol}{\boldsymbol{a}}$.  

$\textbf{s1}=\textbf{'be'}$ 

$s2=\text{'cat'}$  

These do not share a substring.  

Function Description

Complete the function twoStrings in the editor below.    

twoStrings has the following parameter(s):  

string s1:  a string
string s2:  another string    

Returns  

string: either YES or NO

Input Format

The first line contains a single integer $\boldsymbol{p}$, the number of test cases.     

The following $\boldsymbol{p}$ pairs of lines are as follows:

The first line contains string $\mbox{s1}$.
The second line contains string $\mbox{s2}$.

Constraints

$\mbox{s1}$ and $\mbox{s2}$ consist of characters in the range ascii[a-z].
$1\leq p\leq10$
$1\leq|s1|,|s2|\leq10^5$

Output Format

For each pair of strings, return YES or NO.

Sample Input
2
hello
world
hi
world

Sample Output
YES
NO

Explanation

We have $p=2$ pairs to check:

$s1=\text{"hello"}$, $s2=\text{"world"}$. The substrings $\text{"o"}$ and $\text{"l"}$  are common to both strings.  
$a=\textsf{hi}$, $b=\text{"world"}$. $\mbox{s1}$ and $\mbox{s2}$ share no common substrings.
"""

def two_strings(s1: str, s2: str) -> str:
    # Convert both strings to sets of characters
    set_s1 = set(s1)
    set_s2 = set(s2)
    
    # Check for intersection of the sets
    if set_s1.intersection(set_s2):
        return "YES"
    else:
        return "NO"