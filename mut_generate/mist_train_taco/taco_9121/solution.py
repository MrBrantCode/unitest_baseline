"""
QUESTION:
You are given a list of $N$ numbers $a_1,a_2,\ldots,a_n$. For each element at position $\boldsymbol{i}$ ($1\leq i\leq N$), we define $\text{Left}(i)$ and $\textit{Right}(i)$ as: 

$\text{Left}(i)$ = closest index j such that j < i and $a_j>a_i$. If no such j exists then $\text{Left}(i)$ = 0. 

$\textit{Right}(i)$ = closest index k such that k > i and $a_k>a_i$. If no such k exists then $\textit{Right}(i)$ = 0.   

We define $\textit{IndexProduct(i)}$ = $\text{Left}(i)$ * $\textit{Right}(i)$. You need to find out the maximum $\textit{IndexProduct(i)}$ among all i.

Input Format

The first line contains an integer $N$, the number of integers.
The next line contains the $N$ integers describing the list a[1..N].

Constraints 

$1\leq N\leq10^5$ 

$1\leq a_i\leq10^9$

Output Format

Output the maximum $\textit{IndexProduct}$ among all indices from $1$ to $N$. 

Sample Input
5
5 4 3 4 5

Sample Output
8

Explanation

We can compute the following:

$IndexProduct(1)=0$ 

$IndexProduct(2)=1\times5=5$ 

$IndexProduct(3)=2\times4=8$ 

$IndexProduct(4)=1\times5=5$ 

$IndexProduct(5)=0$

The largest of these is 8, so it is the answer.
"""

def max_index_product(arr):
    def lefts(L):
        left = []
        maxes = []
        for i in range(len(L)):
            while maxes and L[maxes[-1]] <= L[i]:
                maxes.pop()
            if not maxes:
                left.append(0)
            else:
                left.append(maxes[-1] + 1)
            maxes.append(i)
        return left

    def rights(L):
        right = []
        maxes = []
        for i in range(len(L) - 1, -1, -1):
            while maxes and L[maxes[-1]] <= L[i]:
                maxes.pop()
            if not maxes:
                right.append(0)
            else:
                right.append(maxes[-1] + 1)
            maxes.append(i)
        right.reverse()
        return right

    left = lefts(arr)
    right = rights(arr)
    products = [left[i] * right[i] for i in range(len(arr))]
    return max(products)