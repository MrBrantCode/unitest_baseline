"""
QUESTION:
Watson gives Sherlock an array $\mbox{A}$ of $N$ elements and two arrays $\mbox{B}$ and $\mbox{C}$, of $\mbox{M}$ elements each. Then he asks Sherlock to perform the following program:

for i = 1 to M do
    for j = 1 to N do
        if j % B[i] == 0 then
            A[j] = A[j] * C[i]
        endif
    end do
end do

This code needs to be optimized. Can you help Sherlock and tell him the resulting array $\mbox{A}$? You should print all the array elements modulo $(10^9+7)$.

Input Format 

The first line contains two integer, $N$ and $\mbox{M}$. The next line contains $N$ integers, the elements of array $\mbox{A}$. The last two lines contain $\mbox{M}$ integers each, the elements of array $\mbox{B}$ and $\mbox{C}$, respectively.

Output Format 

Print $N$ space-separated integers, the elements of array $\mbox{A}$ after performing the program modulo $(10^9+7)$.

Constraints 

$1\leq N,M\leq10^5$ 

$1\leq B[i]\leq N$ 

$1\leq A[i],C[i]\leq10^5$

Sample Input

4 3
1 2 3 4
1 2 3
13 29 71

Sample Output

13 754 2769 1508
"""

def optimize_array(n, m, A, B, C):
    mod = 10 ** 9 + 7
    tmp = [-1] * (n + 1)
    
    for i in range(m):
        if tmp[B[i]] == -1:
            tmp[B[i]] = C[i]
        else:
            tmp[B[i]] *= C[i]
            tmp[B[i]] %= mod
    
    for i in range(1, n + 1):
        if tmp[i] >= 0:
            for j in range(1, n // i + 1):
                A[i * j - 1] *= tmp[i]
                A[i * j - 1] %= mod
    
    return A