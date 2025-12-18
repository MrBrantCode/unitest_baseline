"""
QUESTION:
Consider the following pseudocode, run on an array $A=[a_0,a_1,...,a_{n-1}]$ of length $n$:

rep := 0
while A not empty:
    B := []
    for x in A, y in A:
        if x != y: append absolute_value(x - y) to B
    A := B
    rep := rep + 1

Given the values of $n$ and array $\mbox{A}$, compute and print the final value of ${\mbox{rep}}$ after the pseudocode above terminates; if the loop will never terminate, print -1 instead.

Input Format

The first line contains a single integer, $n$, denoting the length of array $\mbox{A}$. 

The second line contains $n$ space-separated integers describing the respective values of $a_0,a_1,\ldots,a_{n-1}$.

Constraints

$1\leq n\leq10^5$  
$1\leq a_i\leq5\times10^4\ \text{}\forall\ 1\leq i\leq n$

Output Format

Print the final value of ${\mbox{rep}}$ after the pseudocode terminates; if the loop will never terminate, print -1 instead.

Sample Input 0
3
1 3 4

Sample Output 0
4

Explanation 0

After the first loop, $\mbox{A}$ becomes $[2,3,2,1,3,1]$. After the second loop, the array only contains $\mbox{1}$'s and $2$'s. After the third loop, the array only contains $\mbox{1}$'s. After the fourth loop, the array is empty. Because the value of ${\mbox{rep}}$ is incremented after each loop, $rep=4$ at the time the loop terminates. Thus, we print 4 as our answer.
"""

def compute_final_rep(A, n):
    if type(A) == set:
        A = sorted(list(A))
    
    if len(A) == 1:
        return 1
    
    rep = 0
    while len(A) > 0:
        if len(A) == 1:
            return rep + 1
        
        LCM = True
        for i1 in A[1:]:
            if i1 % A[0] != 0:
                LCM = False
                break
        
        if LCM:
            A = [int(m / A[0]) for m in A]
        
        if A[0] == 1 and A[1] == 2:
            return rep + A[-1]
        
        Delta = set()
        if len(A) < 100:
            MaxWidth = len(A) - 1
        else:
            MaxWidth = int(len(A) ** 0.75 // 1)
        
        for W in range(1, MaxWidth + 1):
            for i1 in range(len(A) - W):
                Delta.add(abs(A[i1 + W] - A[i1]))
        
        Delta = sorted(list(Delta))
        A = sorted(list(set([m for m in Delta] + [A[-1] - m for m in A[:-1]])))
        
        rep += 1
    
    return rep