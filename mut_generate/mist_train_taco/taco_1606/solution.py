"""
QUESTION:
You are given a function $f(X)=X^2$. You are also given $\mbox{K}$ lists. The $i^{\mbox{th}}$ list consists of $N_i$ elements.

You have to pick one element from each list so that the value from the equation below is maximized: 

$S=(f(X_1)~+f(X_2)+~....~+f(X_k))$%$\mbox{M}$

$X_i$ denotes the element picked from the $i^{\mbox{th}}$ list . Find the maximized value $S_{max}$  obtained. 

$\gamma_{0}$ denotes the modulo operator. 

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem. 

Input Format

The first line contains $2$ space separated integers $\mbox{K}$ and $\mbox{M}$. 

The next $\mbox{K}$ lines each contains an integer $N_i$, denoting the number of elements in the $i^{\mbox{th}}$ list, followed by $N_i$ space separated integers denoting the elements in the list. 

Constraints

$1\leq K\leq7$ 

$1\leq M\leq1000$ 

$1\leq N_i\leq7$ 

$1\le\textit{Magnitude of elements in list}\le10^9$  

Output Format

Output a single integer denoting the value $S_{max}$. 

Sample Input
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output
206

Explanation

Picking $5$ from the $\mbox{I}$^{st} list, $\mbox{9}$ from the $2$^{nd} list and $10$ from the $3$^{rd} list gives the maximum $\mbox{S}$ value equal to $(5^2+9^2+10^2)$%$\textbf{1000}$ = $\textbf{206}$.
"""

from itertools import product

def maximize_modulo_sum(K, M, lists):
    # Extract the elements from each list (ignoring the first element which is the count)
    elements_lists = [lst[1:] for lst in lists]
    
    # Calculate the maximum sum of squares modulo M
    S_max = max((sum((x ** 2 for x in val)) % M for val in product(*elements_lists)))
    
    return S_max