"""
QUESTION:
The median of a sequence is the element in the middle of the sequence after it is sorted. For a sequence with even size, the median is the average of the two middle elements of the sequence after sorting. For example, for a sequence $A = [1, 3, 3, 5, 4, 7, 11]$, the median is equal to $4$, and for $A = [2, 3, 4, 5]$, the median is equal to $(3+4)/2 = 3.5$.
Fulu is a famous programmer in his country. He wrote the following program (given in pseudocode) for finding the median in a sequence $A$ with length $N$:
read(N)
read(A[0], A[1], ..., A[N-1])
sort(A)
# simultaneously remove elements A[K] and A[N mod K] from the array A
# the order of the remaining N-2 elements is unchanged
remove(A[K], A[N mod K])
return A[(N-2)/2] # integer division

The program takes an integer $K$ as a parameter. Fulu can choose this integer arbitrarily between $1$ and $N-1$ inclusive.
Little Lima, Fulu's friend, thinks Fulu's program is wrong (as always). As finding one counterexample would be an easy task for Lima (he has already found the sequence $A = [34, 23, 35, 514]$, which is a counterexample for any $K \le 3$), Lima decided to make hacking more interesting. Fulu should give him four parameters $S, K, m, M$ (in addition to $N$) and Lima should find the lexicographically smallest proper sequence $A$ with length $N$ as a counterexample.
We say that a sequence $A$ with length $N$ ($0$-indexed) is proper if it satisfies the following conditions:
- it contains only positive integers
- $A_0 + A_1 +A_2 + \dots + A_{N-1} = S$
- $m \le A_i \le M$ for each $0 \le i < N$
- the number returned by Fulu's program, ran with the given parameter $K$, is different from the correct median of the sequence $A$
Can you help Lima find the lexicographically smallest counterexample or determine that Fulu's program works perfectly for the given parameters?

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains five space-separated integers $N$, $S$, $K$, $m$ and $M$.

-----Output-----
For each test case, if there is no proper sequence, print a single line containing the integer $-1$; otherwise, print a single line containing $N$ space-separated integers — the lexicographically smallest proper sequence.

-----Constraints-----
- $1 \le T \le 8$
- $3 \le N \le 10^5$
- $1 \le K \le N-1$
- $1 \le S \le 10^9$
- $1 \le m \le M \le S$

-----Example Input-----
2
3 6 1 1 5
4 4 2 1 3

-----Example Output-----
1 1 4
-1

-----Explanation-----
Example case 1: For the sequence $A = [1, 1, 4]$, it is already sorted, so the program would just remove the first two elements ($K=1$, $N\%K=0$) and return the only remaining element $4$. Obviously, the median of the original sequence is $1$. It can be shown that there is no lexicographically smaller proper sequence.
Example case 2: The only possible sequence is $A = [1, 1, 1, 1]$, which is not proper, since Fulu's program will give the correct answer $1$ for it.
"""

def find_lexicographically_smallest_counterexample(N, S, K, m, M):
    def gen_best_seq(n, diff_ind, m, M, s):
        arr = np.full((n,), m)
        arr[diff_ind:] += 1
        s = s - np.sum(arr)
        if s < 0:
            return -1
        inc = M - m - 1
        ind = n - 1
        while ind >= 0:
            z = min(inc, s)
            arr[ind] += z
            s -= z
            ind -= 1
        if s != 0:
            return -1
        return arr

    def test_seq(k, seq):
        seq = sorted(seq)
        n = len(seq)
        if n % 2 == 1:
            median = seq[n // 2]
        else:
            median = (seq[n // 2 - 1] + seq[n // 2]) / 2
        seq.pop(n % k)
        seq.pop(k - 1)
        return median != seq[(n - 2) // 2]

    mid_ind = N // 2
    seqs = []
    for ind in range(mid_ind + 2, mid_ind - 3, -1):
        if ind >= N or ind < 0:
            continue
        seq = gen_best_seq(N, ind, m, M, S)
        if seq is not -1 and test_seq(K, seq):
            seqs.append(list(seq))
    if len(seqs) == 0:
        return -1
    return min(seqs)