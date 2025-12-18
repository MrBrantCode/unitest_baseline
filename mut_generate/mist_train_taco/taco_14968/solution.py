"""
QUESTION:
There is a binary string S. Alice and Bob are playing a game on it.

Each turn, the following happens:

1. Alice selects a 01 subsequence in S and removes it from S. (a 01 subsequence is a length 2 subsequence whose first character is 0 and second character is 1)
2. Bob selects a 01 subsequence in S and removes it from S.
3. After both players have moved, the turn is called completed and Alice scores 1 point. Then, the next turn begins.

If either player is unable to move (there isn't any 01 subsequence left in S), that turn ends immediately and the game ends.

Alice tries to maximize her points, while Bob tries to minimize Alice's points. Find how many points Alice would score if both players play optimally.

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. 
- Each of the next T lines contains a binary string S.

------ Output Format ------ 

For each test case, output on a new line a single integer — Alice's score when both players play optimally.

------ Constraints ------ 

$1 ≤ T ≤ 2\cdot 10^{5}$
- The sum of $|S|$ across all tests doesn't exceed  $2 \cdot 10^{5}$

------ subtasks ------ 

Subtask 1 (25 Points):
The sum of $|S|$ across all tests doesn't exceed $100$
Subtask 2 (25 Points):
The sum of $|S|$ across all tests doesn't exceed $1500$
Subtask 3 (50 Points):
No further constraints.

----- Sample Input 1 ------ 
4
01010101
0101
10
01001011

----- Sample Output 1 ------ 
1 
1 
0 
2 

----- explanation 1 ------ 
In the first example, this is one of the possible outcomes.

Turn $1$:
- Alice removes subsequence $(1, 2)$ from $S$, so $S$ becomes 010101.
- Bob removes subsequence $(3, 6)$ from $S$, so $S$ becomes 0110.
- Alice scores one point and the first turn ends.

Turn 2:
- Alice removes subsequence $(1, 2)$ from $S$, so $S$ becomes 10.
- Bob has nothing to do, so the game ends immediately.

Thus, Alice has one point in total.
"""

def calculate_alice_score(S: str) -> int:
    N = len(S)
    pos0 = []
    pos1 = []
    
    # Collect positions of '0' and '1' in the string
    for i in range(N):
        if S[i] == '0':
            pos0.append(i)
        elif S[i] == '1':
            pos1.append(i)
        else:
            assert False  # This should never happen with a valid binary string

    # Helper function to determine if a given number of turns is feasible
    def is_good(num_turns: int) -> bool:
        if num_turns * 2 > min(len(pos0), len(pos1)):
            return False
        for c0 in range(num_turns + 1):
            c1 = num_turns - c0
            cur_0 = num_turns + c0 - 1
            cur_1 = len(pos1) - (num_turns + c1)
            p1 = len(pos1) - 1 - (num_turns + c1)
            p0 = num_turns + c0
            num_0 = c0
            num_1 = c1
            split_good = True
            for t in range(num_turns):
                if pos0[cur_0] < pos1[cur_1]:
                    cur_0 -= 1
                    cur_1 += 1
                else:
                    split_good = False
                    break
                if num_1 > 0 and pos0[p0] < pos1[cur_1]:
                    p0 += 1
                    cur_1 += 1
                    num_1 -= 1
                elif num_0 > 0 and pos0[cur_0] < pos1[p1]:
                    cur_0 -= 1
                    p1 -= 1
                    num_0 -= 1
                else:
                    split_good = False
                    break
            if split_good:
                return True
        return False

    # Binary search to find the maximum number of turns Alice can achieve
    mi = 0
    ma = min(len(pos0), len(pos1)) // 2 + 1
    while ma - mi > 1:
        md = (mi + ma) // 2
        if is_good(md):
            mi = md
        else:
            ma = md
    
    return mi