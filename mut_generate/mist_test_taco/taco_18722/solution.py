"""
QUESTION:
You are given $N$ integers in an array: $A[1], A[2], \ldots, A[N]$. You also have another integer $L$.
Consider a sequence of indices ($i_1, i_2, \ldots, i_k$). Note that a particular index can occur multiple times in the sequence, and there is no order in which these indices have to occur. ($i_1, i_2, \ldots, i_k$) is a sequence of size $k$. It is said to be an $Interesting$ sequence, if $A[i_1] \ge A[i_2] \ge \ldots \ge A[i_k]$.
The $Cost$ of an Interesting sequence ($i_1, i_2, \ldots, i_k$), is defined to be the minimum absolute difference between any two adjacent indices. In other words, the Cost is $min \{ |i_2 - i_1|, |i_3 - i_2|, \ldots, |i_k - i_{k-1}| \}$.
Your job is to consider the Costs of all the Interesting sequences of size $L$ associated with the given array, and output the maximum Cost. Note that you can show that there is always at least one Interesting sequence for the given constraints.

-----Input-----
- The first line contains a single integer, $T$, which is the number of testcases. The description of each testcase follows.
- The first line of each testcase contains two space separated integers: $N$ and $L$.
- The second line of each testcase contains $N$ space separated integers: $A[1], A[2], \ldots, A[N]$.

-----Output-----
- For each testcase, output the answer in a new line.

-----Constraints-----
- $1 \leq T \leq 3$
- $1 \leq A[i] \leq 10^9$
- $2 \leq L \leq 10^9$

-----Subtasks-----
- Subtask 1: 7 points
- It is guaranteed that $A[1] > A[2] > \ldots > A[N]$
- Note that the above condition implies that all elements are distinct.
- $1 \leq N \leq 500$
- Subtask 2: 7 points
- It is guaranteed that $A[1] \ge A[2] \ge \ldots \ge A[N]$
- $1 \leq N \leq 500$
- Subtask 3: 14 points
- It is guaranteed that all elements are distinct.
- $1 \leq N \leq 500$
- Subtask 4: 14 points
- $1 \leq N \leq 500$
- Subtask 5: 25 points
- It is guaranteed that all elements are distinct.
- $1 \leq N \leq 3000$
- Subtask 6: 33 points
- $1 \leq N \leq 3000$

-----Sample Input-----
1
6 3
2 4 1 12 3 5

-----Sample Output-----
3

-----Explanation-----
We are looking for Interesting sequences of length 3. Some of them are:
- (4, 2, 3): This is Interesting because $A[4] \ge A[2] \ge A[3]$. Its cost is $min \{ |2-4|, |3-2|\} = 1$.
- (5, 1, 1): Cost is 0.
- (2, 2, 2): Cost is 0.
- (6, 1, 3): Cost is 2.
- (6, 2, 5): Cost is 3.
There are other Interesting Sequences of length 3 as well. But if you list them all out, you'll see that the maximum Cost is 3. Hence the answer is 3.
"""

def find_max_interesting_sequence_cost(N, L, A):
    def insort(l, v):
        s = 0
        e = len(l)
        while True:
            mid = (s + e) // 2
            if s == e or mid > len(l):
                break
            if l[mid][0] < v[0]:
                s = mid + 1
            elif l[mid][0] > v[0]:
                e = mid
            else:
                break
        l.insert(mid, v)

    dic = {}
    dif = 0
    for i, v in enumerate(A, start=1):
        if v not in dic:
            dic[v] = [i, i]
        else:
            dic[v][0] = min(dic[v][0], i)
            dic[v][1] = max(dic[v][1], i)
            dif = max(dif, dic[v][1] - dic[v][0])
    
    ans = dif
    if L <= len(set(A)):
        i_l = [[v, i] for i, v in enumerate(A, start=1)]
        i_l.sort(reverse=True)
        dp = [[-1 for _ in range(L)] for _ in range(N)]
        pq_l = [[] for _ in range(L)]
        for i in range(1, N):
            il = 1
            dif_l = []
            for j in range(i):
                dif = abs(i_l[i][1] - i_l[j][1])
                dif_l.append(dif)
                dp[i][il] = max(dp[i][il], dif)
            for il in range(2, min(L, i + 1)):
                for prev_max, ind in reversed(pq_l[il - 1]):
                    if ind == i:
                        continue
                    if prev_max < dp[i][il]:
                        break
                    else:
                        dp[i][il] = max(dp[i][il], min(dif_l[ind], prev_max))
                insort(pq_l[il], [dp[i][il], i])
            il = 1
            insort(pq_l[il], [dp[i][il], i])
            ans = max(ans, dp[i][-1])
    
    return ans