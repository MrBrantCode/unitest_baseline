"""
QUESTION:
We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank.  Remeber that a subsequence maintains the order of characters selected from a sequence.   

More formally, let $p[0],p[1],\cdots,p[9]$ be the respective indices of h, a, c, k, e, r, r, a, n, k in string $\boldsymbol{\mathrm{~S~}}$. If $p[0]<p[1]<p[2]<\text{...}<p[9]$ is true, then $\boldsymbol{\mathrm{~S~}}$ contains hackerrank.

For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.  

Example 

$s=\text{haacckker}\text{rannkk}$  

This contains a subsequence of all of the characters in the proper order.  Answer YES  

$s=\text{haacckkerannk}$  

This is missing the second 'r'.  Answer NO.  

$s=\text{hccaakker}\text{rannkk}$  

There is no 'c' after the first occurrence of an 'a', so answer NO.  

Function Description  

Complete the hackerrankInString function in the editor below.   

hackerrankInString has the following parameter(s):  

string s: a string   

Returns  

string: YES or NO

Input Format

The first line contains an integer $\textit{q}$, the number of queries. 

Each of the next $\textit{q}$ lines contains a single query string $\boldsymbol{\mathrm{~S~}}$.  

Constraints

$2\leq q\leq10^2$  
$10\leq\:\text{length of}\:s\leq10^4$

Sample Input 0
2
hereiamstackerrank
hackerworld

Sample Output 0
YES
NO

Explanation 0

We perform the following $q=2$ queries:

$s=\textbf{hereiamstacker}\textbf{rank}$ 

The characters of hackerrank are bolded in the string above. Because the string contains all the characters in hackerrank in the same exact order as they appear in hackerrank, we return YES.
$s=\textbf{hackerworld}$ does not contain the last three characters of hackerrank, so we return NO.

Sample Input 1
2
hhaacckkekraraannk
rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt

Sample Output 1
YES
NO



The diagram below depicts our map of Hackerland:

We can cover the entire city by installing $3$ transmitters on houses at locations $\begin{array}{c}4\end{array}$, $\mbox{9}$, and $12$.
"""

def contains_hackerrank(s: str) -> str:
    pattern = '.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*'
    if re.search(pattern, s):
        return 'YES'
    else:
        return 'NO'