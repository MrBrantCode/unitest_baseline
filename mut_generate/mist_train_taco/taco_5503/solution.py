"""
QUESTION:
This is a rather simple problem to describe. You will be given three numbers $S, P$ and $k$. Your task is to find if there are integers $n_1, n_2,...,n_k$ such that $n_1 + n_2 +...+ n_k = S$, $n_1 \cdot n_2 \cdot ... \cdot n_k = P$. If such integers exist, print them out. If no such sequence of integers exist, then print "NO".
For example if $S=11, P=48$ and $k=3$ then $3, 4$ and $4$ is a solution. On the other hand, if $S=11, P=100$ and $k=3$, there is no solution and you should print "NO".

-----Input:-----
A single line with three integers $S, P$ and $k$.

-----Output:-----
A single word "NO" or a seqence of $k$ integers $n_1, n_2,..., n_k$ on a single line. (The $n_i$'s must add up to $S$ and their product must be $P$).

-----Constraints:-----
- $1 \leq k \leq 4$.
- $1 \leq S \leq 1000$.
- $1 \leq P \leq 1000$.

-----Sample input 1:-----
11 48 3

-----Sample output 1:-----
3 4 4 

-----Sample input 2:-----
11 100 3

-----Sample output 2:-----
NO
"""

def find_integer_combination(S, P, k):
    def findCombo(s, p, k):
        if k == 1:
            if s == p:
                return [s]
            else:
                return []
        else:
            for i in range(1, s):
                if p % i == 0 and i < s:
                    ans = findCombo(s - i, p // i, k - 1)
                    if len(ans) != 0:
                        ans.append(i)
                        return ans
            return []
    
    ans = findCombo(S, P, k)
    if len(ans) == 0:
        return "NO"
    else:
        return ans