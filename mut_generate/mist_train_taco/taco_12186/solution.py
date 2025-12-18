"""
QUESTION:
Chef has a sequence $A_1, A_2, \ldots, A_N$. This sequence has exactly $2^N$ subsequences. Chef considers a subsequence of $A$ interesting if its size is exactly $K$ and the sum of all its elements is minimum possible, i.e. there is no subsequence with size $K$ which has a smaller sum.
Help Chef find the number of interesting subsequences of the sequence $A$.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Output-----
For each test case, print a single line containing one integer ― the number of interesting subsequences.

-----Constraints-----
- $1 \le T \le 10$
- $1 \le K \le N \le 50$
- $1 \le A_i \le 100$ for each valid $i$

-----Subtasks-----
Subtask #1 (30 points): $1 \le N \le 20$
Subtask #2 (70 points): original constraints

-----Example Input-----
1
4 2
1 2 3 4

-----Example Output-----
1

-----Explanation-----
Example case 1: There are six subsequences with length $2$: $(1, 2)$, $(1, 3)$, $(1, 4)$, $(2, 3)$, $(2, 4)$ and $(3, 4)$. The minimum sum is $3$ and the only subsequence with this sum is $(1, 2)$.
"""

from math import factorial

def count_interesting_subsequences(N, K, A):
    # Sort the original array
    A.sort()
    
    # Get the first K elements (minimum sum subsequence candidates)
    cut_arr = A[:K]
    
    # Get unique elements in the cut array
    unq = list(set(cut_arr))
    
    # Calculate frequencies of unique elements in the original and cut arrays
    freq_or = []
    freq_cut = []
    for x in unq:
        freq_or.append(A.count(x))
        freq_cut.append(cut_arr.count(x))
    
    # Calculate the number of interesting subsequences
    summ = 1
    for x in range(len(unq)):
        N_fact = factorial(freq_or[x])
        R_fact = factorial(freq_cut[x])
        N_R_fact = factorial(freq_or[x] - freq_cut[x])
        summ *= (N_fact // (N_R_fact * R_fact))
    
    return int(summ)