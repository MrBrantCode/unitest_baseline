"""
QUESTION:
Chef is given a sequence of prime numbers $A_1, A_2, \ldots, A_N$. This sequence has exactly $2^N$ subsequences. A subsequence of $A$ is good if it does not contain any two identical numbers; in particular, the empty sequence is good.
Chef has to find the number of good subsequences which contain at most $K$ numbers. Since he does not know much about subsequences, help him find the answer. This number could be very large, so compute it modulo $1,000,000,007$.

-----Input-----
- The first line of the input contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Output-----
Print a single line containing one integer ― the number of good subsequences with size at most $K$, modulo $1,000,000,007$.

-----Constraints-----
- $1 \le K \le N \le 10^5$
- $2 \le A_i \le 8,000$ for each valid $i$

-----Subtasks-----
Subtask #1 (40 points): $A_1, A_2, \ldots, A_N$ are pairwise distinct
Subtask #2 (60 points): original constraints

-----Example Input-----
5 3
2 2 3 3 5

-----Example Output-----
18

-----Explanation-----
There is $1$ good subsequence with length $0$, $5$ good subsequences with length $1$, $8$ good subsequences with length $2$ and $4$ good subsequences with length $3$.
"""

from collections import Counter
from itertools import accumulate

def count_good_subsequences(N, K, A):
    MOD = 10**9 + 7
    
    # Count the frequency of each number in the sequence
    ctr = Counter(A)
    
    # Get the unique numbers in the sequence
    st = list(set(A))
    l = len(st)
    
    # Adjust K to be the minimum of K and the number of unique elements
    K = min(K, l)
    
    # Calculate the prefix sums of the counts
    m = list(accumulate([ctr[i] for i in st]))
    
    ans = 0
    
    # Calculate the number of good subsequences for each length from 2 to K
    for i in range(2, K + 1):
        temp = []
        for j in range(l):
            if j >= i - 1:
                ans += m[j - 1] * ctr[st[j]]
                temp.append(m[j - 1] * ctr[st[j]] + (temp[-1] if temp else 0))
            else:
                temp.append(0)
        m = temp
    
    # Add the counts for subsequences of length 0, 1, and the results from the loop
    ans = (ans + sum(ctr.values()) + 1) % MOD
    
    return ans