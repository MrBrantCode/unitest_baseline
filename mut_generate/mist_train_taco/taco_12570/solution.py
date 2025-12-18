"""
QUESTION:
Rhezo is the new manager of Specialist Cinema Hall. A new movie is being released this Friday and Rhezo wants people in the hall to be seated according to some rules. His rules are weird and he likes that no 2 people in a row sit together/adjacent. He also wants that there are at least 2 people in each row. 

The hall should have at least K people in it, if there are less the show gets cancelled. The hall can be visualised as a N \times M matrix. Rhezo wants to find the number of different seating arrangements of people in it. Two seating arrangements are different if there is at least one seat which is filled in one arrangement and vacant in other. 

You being Rhezo's best friend, want to help him in this task. As the number can be large, output your answer modulo 10^9+7.

Input:

First line of input contains 2 integers N and M. Second line contains a single integer K.

Output:

Find the number of different arrangements of people in the hall satisfying the constraints given in problem statement. Output your answer modulo 10^9+7.

Constraints:

1 ≤ N, K ≤ 500

1 ≤ M ≤ 10

SAMPLE INPUT
1 5 2

SAMPLE OUTPUT
7

Explanation

Following are the 7 different seating arrangements:

x.x.x

..x.x

.x..x

.x.x.

x...x

x..x.

x.x..
"""

MOD = 1000000007

def calculate_seating_arrangements(N, M, K):
    # Precomputed combinations for rows of length M
    combs = {
        3: {2: 1},
        4: {2: 3},
        5: {2: 6, 3: 1},
        6: {2: 10, 3: 4},
        7: {2: 15, 3: 10, 4: 1},
        8: {2: 21, 3: 20, 4: 5},
        9: {2: 28, 3: 35, 4: 15, 5: 1},
        10: {2: 36, 3: 56, 4: 35, 5: 6}
    }
    
    # Initial combinations for a single row
    actcombs = {1: combs[M]}
    numrows = 1
    
    # Double the number of rows until we reach or exceed N
    while numrows * 2 <= N:
        newcombs = {}
        lastcombs = actcombs[numrows]
        for i in lastcombs:
            for j in lastcombs:
                toadd = (lastcombs[i] * lastcombs[j]) % MOD
                newcombs[i + j] = (newcombs[i + j] + toadd) % MOD if i + j in newcombs else toadd
        numrows *= 2
        actcombs[numrows] = newcombs
    
    # Combine the rows to get the final result
    newcombs = {0: 1}
    actrows = 0
    for i in reversed(sorted(actcombs.keys())):
        if actrows + i <= N:
            lastcombs = newcombs
            newcombs = {}
            for k1 in lastcombs:
                for k2 in actcombs[i]:
                    toadd = (lastcombs[k1] * actcombs[i][k2]) % MOD
                    newcombs[k1 + k2] = (newcombs[k1 + k2] + toadd) % MOD if k1 + k2 in newcombs else toadd
            actrows += i
    
    # Calculate the total number of valid arrangements
    total = 0
    for i in range(K, N * M + 1):
        if i in newcombs:
            total = (total + newcombs[i]) % MOD
    
    return total