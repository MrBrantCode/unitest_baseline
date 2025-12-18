"""
QUESTION:
A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.  Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length, which is common to both the sequences. 

Given two sequences of integers, $A=[a[1],a[2],...,a[n]]$ and $B=[b[1],b[2],...,b[m]]$, find the longest common subsequence and print it as a line of space-separated integers. If there are multiple common subsequences with the same maximum length, print any one of them.

In case multiple solutions exist, print any of them. It is guaranteed that at least one non-empty common subsequence will exist.    

Recommended References  

This Youtube video tutorial explains the problem and its solution quite well.  

Function Description  

Complete the longestCommonSubsequence function in the editor below.  It should return an integer array of a longest common subsequence.  

longestCommonSubsequence has the following parameter(s):  

a: an array of integers  
b: an array of integers

Input Format

The first line contains two space separated integers $n$ and $m$, the sizes of sequences $\mbox{A}$ and $\mbox{B}$. 

The next line contains $n$ space-separated integers $A[i]$. 

The next line contains $m$ space-separated integers $B[j]$.

Constraints  

$1\leq n\leq100$ 

$1\leq m\leq100$ 

$0\leq a[i]<1000,\ \text{where}\ i\in[1,n]$ 

$0\leq b[j]<1000,\ \text{where}\ j\in[1,m]$  

Constraints

$1\le n,m\le100$ 

$0\leq a[i],b[j]<1000$  

Output Format

Print the longest common subsequence as a series of space-separated integers on one line. In case of multiple valid answers, print any one of them.

Sample Input
5 6
1 2 3 4 1
3 4 1 2 1 3

Sample Output
1 2 3

Explanation

There is no common subsequence with length larger than 3. And "1 2 3",  "1 2 1", "3 4 1" are all correct answers.  

Tested by Khongor
"""

def longest_common_subsequence(a, b):
    xLength = len(a)
    yLength = len(b)
    
    # Initialize the table for dynamic programming
    table = [[0] * (yLength + 1) for _ in range(xLength + 1)]
    
    # Fill the table
    for i in range(1, xLength + 1):
        for j in range(1, yLength + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    
    # Retrieve the LCS from the table
    LCS = []
    i, j = xLength, yLength
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            LCS.append(a[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # The LCS is built in reverse order, so reverse it before returning
    LCS.reverse()
    return LCS