"""
QUESTION:
There is a building with 2N floors, numbered 1, 2, \ldots, 2N from bottom to top.
The elevator in this building moved from Floor 1 to Floor 2N just once.
On the way, N persons got on and off the elevator. Each person i (1 \leq i \leq N) got on at Floor A_i and off at Floor B_i. Here, 1 \leq A_i < B_i \leq 2N, and just one person got on or off at each floor.
Additionally, because of their difficult personalities, the following condition was satisfied:
 - Let C_i (= B_i - A_i - 1) be the number of times, while Person i were on the elevator, other persons got on or off. Then, the following holds:
 - If there was a moment when both Person i and Person j were on the elevator, C_i = C_j.
We recorded the sequences A and B, but unfortunately, we have lost some of the records. If the record of A_i or B_i is lost, it will be given to you as -1.
Additionally, the remaining records may be incorrect.
Determine whether there is a pair of A and B that is consistent with the remaining records.

-----Constraints-----
 - 1 \leq N \leq 100
 - A_i = -1 or 1 \leq A_i \leq 2N.
 - B_i = -1 or 1 \leq B_i \leq 2N.
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 B_1
A_2 B_2
:
A_N B_N

-----Output-----
If there is a pair of A and B that is consistent with the remaining records, print Yes; otherwise, print No.

-----Sample Input-----
3
1 -1
-1 4
-1 6

-----Sample Output-----
Yes

For example, if B_1 = 3, A_2 = 2, and A_3 = 5, all the requirements are met.
In this case, there is a moment when both Person 1 and Person 2 were on the elevator, which is fine since C_1 = C_2 = 1.
"""

def is_consistent_elevator_records(N, A, B):
    L = 2 * N
    floor = [[0, 0] for _ in range(L)]
    com = dict()
    
    for i in range(1, N + 1):
        Ai = A[i - 1]
        Bi = B[i - 1]
        com[i] = [-1, -1]
        
        if Ai != -1:
            if floor[Ai - 1][1] == 0:
                floor[Ai - 1] = [i, 1]
                com[i][0] = Ai - 1
            else:
                return False
        
        if Bi != -1:
            if floor[Bi - 1][1] == 0:
                floor[Bi - 1] = [i, 2]
                com[i][1] = Bi - 1
            else:
                return False
        
        if Ai != -1 and Bi != -1:
            if Ai >= Bi:
                return False
    
    dp = [False] * (L + 1)
    if floor[0][1] == 2:
        return False
    else:
        dp[0] = True
    
    for i in range(L):
        if not dp[i]:
            continue
        for j in range(i + 1, L, 2):
            ok = True
            w = (j - i + 1) // 2
            for k in range(w):
                p = i + k
                q = i + w + k
                if floor[p][1] == 2 or floor[q][1] == 1:
                    ok = False
                if floor[p][1] == 1 and floor[q][1] == 2:
                    if floor[p][0] != floor[q][0]:
                        ok = False
                if floor[p][1] == 1:
                    f = floor[p][0]
                    if com[f][1] != q and com[f][1] != -1:
                        ok = False
                if floor[q][1] == 2:
                    f = floor[q][0]
                    if com[f][0] != p and com[f][0] != -1:
                        ok = False
            if ok:
                dp[j + 1] = True
    
    return dp[L]