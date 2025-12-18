"""
QUESTION:
A gene is represented as a string of length $n$ (where $n$ is divisible by $4$), composed of the letters $\mbox{A}$, $\mbox{C}$, $\textbf{T}$, and $\mbox{G}$.
It is considered to be steady if each of the four letters occurs exactly $\frac{n}{4}$ times.  For example, $\textbf{GACT}$ and $\textbf{AAGTGCCT}$ are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady.  Right now, he is examining a gene represented as a string $\textit{gene}$.  It is not necessarily steady.  Fortunately, Limak can choose one (maybe empty) substring of $\textit{gene}$ and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous.
Given a string $\textit{gene}$, can you help Limak find the length of the smallest possible substring that he can replace to make $\textit{gene}$ a steady gene?

Note: A substring of a string $\boldsymbol{\mathrm{~S~}}$ is a subsequence made up of zero or more contiguous characters of $\boldsymbol{\mathrm{~S~}}$.

As an example, consider $\textit{gene}=\textit{ACTGAAAG}$.  The substring $\boldsymbol{AA}$ just before or after $\mbox{G}$ can be replaced with $\textit{CT}$ or $\boldsymbol{TC}$.  One selection would create $\textbf{ACTGACTG}$.

Function Description

Complete the $\textit{steadyGene}$ function in the editor below.  It should return an integer that represents the length of the smallest substring to replace.  

steadyGene has the following parameter:  

gene: a string

Input Format

The first line contains an interger $n$ divisible by $4$, that denotes the length of a string $\textit{gene}$. 

The second line contains a string $\textit{gene}$ of length $n$.

Constraints

$4\leq n\leq500000$  
$n$ is divisible by $4$  
$gene[i]\in[CGAT]$  

Subtask  

$4\leq n\leq2000$ in tests worth $30\%$ points.

Output Format

Print the length of the minimum length substring that can be replaced to make $\textit{gene}$ stable.

Sample Input
8  
GAAATAAA

Sample Output
5

Explanation

One optimal solution is to replace $\textbf{AAATA}$ with $\textbf{TTCCG}$ resulting in $\textbf{GTTCCGAA}$. 

The replaced substring has length $5$.
"""

def find_min_replacement_length(gene, n=None):
    if n is None:
        n = len(gene)
    
    # Ensure n is divisible by 4
    if n % 4 != 0:
        raise ValueError("The length of the gene must be divisible by 4.")
    
    # Count the occurrences of each character in the gene
    count = {}
    for c in gene:
        count[c] = count.get(c, 0) + 1
    
    # Calculate the required number of each character to make the gene steady
    for c in count:
        if count[c] > n // 4:
            count[c] = count[c] - n // 4
        else:
            count[c] = 0
    
    # If the gene is already steady, return 0
    if sum((count[c] for c in count)) == 0:
        return 0
    
    # Initialize variables for the sliding window approach
    count2 = {}
    i, j, best = 0, 0, n
    
    # Use a sliding window to find the smallest substring that can be replaced
    while j < n:
        while j < n and any((count2.get(c, 0) < count[c] for c in count)):
            count2[gene[j]] = count2.get(gene[j], 0) + 1
            j += 1
        while all((count2.get(c, 0) >= count[c] for c in count)):
            count2[gene[i]] = count2.get(gene[i], 0) - 1
            i += 1
        if j - i + 1 < best:
            best = j - i + 1
    
    return best