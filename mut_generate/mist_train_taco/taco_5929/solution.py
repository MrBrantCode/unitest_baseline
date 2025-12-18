"""
QUESTION:
Alice initially has a string S of length N, and she decides to modify it! Her modification consists of K steps numbered from 1 to K. In the i-th step, Alice reverses the prefix of length i of S.

For example, suppose Alice starts with S = \texttt{abferty}, and she modifies it via 3 steps, then:
After the first step, \textcolor{blue}{\texttt{a}}\texttt{bferty} \rightarrow S = \texttt{abferty}
After the second step, \textcolor{blue}{\texttt{ab}}\texttt{ferty} \rightarrow S = \texttt{baferty}
After the third step, \textcolor{blue}{\texttt{baf}}\texttt{erty} \rightarrow S = \texttt{faberty}
So after 3 steps, her string becomes S = \texttt{faberty}.

After performing her K-step modification, Alice ends up with the string S'. Now she challenges you to find the original string S. Can you do it?

------ Input Format ------ 

- The first line of the input contains a single integer T - the number of test cases. The test cases then follow.
- The first line of the test case contains two space-separated integers N and K - the length of the string and the number of steps in Alice's modification.
- The second line of the test case contains S' - the final string obtained after the modification.

------ Output Format ------ 

For each test case, output the original string S.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 10^{6}$
$1 ≤ K ≤ N$
$|S'| = N$
$S'$ contains only lowercase alphabets
- Sum of $N$ overall cases does not exceed $10^{6}$.

------ subtasks ------ 

Subtask $1$ (30 points): $1 ≤ N \cdot K ≤ 2000$
Subtask $2$ (70 points): Original constraints

----- Sample Input 1 ------ 
3
7 3
faberty
7 5
bbaaaba
4 4
zxwy

----- Sample Output 1 ------ 
abferty
aababba
wxyz

----- explanation 1 ------ 
- Test case $2$: The modification steps from $S$ to $S'$ is as follow:
- $1$-st step: $\textcolor{blue}{\texttt{a}}\texttt{ababba} \rightarrow S = \texttt{aababba}$
- $2$-nd step: $\textcolor{blue}{\texttt{aa}}\texttt{babba} \rightarrow S = \texttt{aababba}$
- $3$-rd step: $\textcolor{blue}{\texttt{aab}}\texttt{abba} \rightarrow S = \texttt{baaabba}$
- $4$-th step: $\textcolor{blue}{\texttt{baaa}}\texttt{bba} \rightarrow S = \texttt{aaabbba}$
- $5$-th step: $\textcolor{blue}{\texttt{aaabb}}\texttt{ba} \rightarrow S = \texttt{bbaaaba}$
- Test case $3$: The modification steps from $S$ to $S'$ is as follow:
- $1$-st step: $\textcolor{blue}{\texttt{w}}\texttt{xyz} \rightarrow S = \texttt{wxyz}$
- $2$-nd step: $\textcolor{blue}{\texttt{wx}}\texttt{yz} \rightarrow S = \texttt{xwyz}$
- $3$-rd step: $\textcolor{blue}{\texttt{xwy}}\texttt{z} \rightarrow S = \texttt{ywxz}$
- $4$-th step: $\textcolor{blue}{\texttt{ywxz}} \rightarrow S = \texttt{zxwy}$
"""

def find_original_string(n, k, s_prime):
    """
    This function finds the original string S given the final string S' after K steps of modification.

    Parameters:
    - n (int): The length of the string.
    - k (int): The number of steps in Alice's modification.
    - s_prime (str): The final string obtained after the modification.

    Returns:
    - str: The original string S.
    """
    beg = 0
    end = k - 1
    res = [''] * n
    
    for i in range(k):
        if not i & 1:
            res[i] = s_prime[beg]
            beg += 1
        else:
            res[i] = s_prime[end]
            end -= 1
    
    res[:k] = res[k - 1::-1]
    
    for i in range(k, n):
        res[i] = s_prime[i]
    
    return ''.join(res)