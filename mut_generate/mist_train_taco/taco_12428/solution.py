"""
QUESTION:
There is a cave consisting of N rooms and M one-directional passages. The rooms are numbered 1 through N.
Takahashi is now in Room 1, and Room N has the exit. The i-th passage connects Room s_i and Room t_i (s_i < t_i) and can only be traversed in the direction from Room s_i to Room t_i. It is known that, for each room except Room N, there is at least one passage going from that room.
Takahashi will escape from the cave. Each time he reaches a room (assume that he has reached Room 1 at the beginning), he will choose a passage uniformly at random from the ones going from that room and take that passage.
Aoki, a friend of Takahashi's, can block one of the passages (or do nothing) before Takahashi leaves Room 1. However, it is not allowed to block a passage so that Takahashi is potentially unable to reach Room N.
Let E be the expected number of passages Takahashi takes before he reaches Room N. Find the value of E when Aoki makes a choice that minimizes E.

-----Constraints-----
 - 2 \leq N \leq 600
 - N-1 \leq M \leq \frac{N(N-1)}{2}
 - s_i < t_i
 - If i != j, (s_i, t_i) \neq (s_j, t_j). (Added 21:23 JST)
 - For every v = 1, 2, ..., N-1, there exists i such that v = s_i.

-----Input-----
Input is given from Standard Input in the following format:
N M
s_1 t_1
:
s_M t_M

-----Output-----
Print the value of E when Aoki makes a choice that minimizes E.
Your output will be judged as correct when the absolute or relative error from the judge's output is at most 10^{-6}.

-----Sample Input-----
4 6
1 4
2 3
1 3
1 2
3 4
2 4

-----Sample Output-----
1.5000000000

If Aoki blocks the passage from Room 1 to Room 2, Takahashi will go along the path 1 → 3 → 4 with probability \frac{1}{2} and 1 → 4 with probability \frac{1}{2}. E = 1.5 here, and this is the minimum possible value of E.
"""

def calculate_minimum_expected_passages(n, m, passages):
    # Initialize the adjacency list
    E = [[] for _ in range(n)]
    for s, t in passages:
        E[s - 1].append(t - 1)
    
    # Dynamic programming array to store expected values
    dp = [0] * n
    
    # Fill dp array from the last room to the first
    for s in range(n - 2, -1, -1):
        for t in E[s]:
            dp[s] += dp[t]
        if E[s]:
            dp[s] /= len(E[s])
        dp[s] += 1
    
    # Initial answer is the expected value without blocking any passage
    ans = dp[0]
    
    # Try blocking each passage and calculate the new expected value
    for s2 in range(n - 1):
        if len(E[s2]) - 1:
            dp2 = [0] * n
            mxi = 0
            mxt = -1
            for t in E[s2]:
                if mxt < dp[t]:
                    mxi = t
                    mxt = dp[t]
            if mxt < 0:
                continue
            for s in range(n - 2, -1, -1):
                for t in E[s]:
                    dp2[s] += dp2[t]
                if s == s2:
                    dp2[s] -= mxt
                if s == s2:
                    dp2[s] /= len(E[s]) - 1
                elif E[s]:
                    dp2[s] /= len(E[s])
                dp2[s] += 1
            ans = min(ans, dp2[0])
    
    return ans