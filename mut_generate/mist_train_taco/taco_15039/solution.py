"""
QUESTION:
The squirrel Chokudai has N acorns. One day, he decides to do some trades in multiple precious metal exchanges to make more acorns.

His plan is as follows:

1. Get out of the nest with N acorns in his hands.
2. Go to Exchange A and do some trades.
3. Go to Exchange B and do some trades.
4. Go to Exchange A and do some trades.
5. Go back to the nest.



In Exchange X (X = A, B), he can perform the following operations any integer number of times (possibly zero) in any order:

* Lose g_{X} acorns and gain 1 gram of gold.
* Gain g_{X} acorns and lose 1 gram of gold.
* Lose s_{X} acorns and gain 1 gram of silver.
* Gain s_{X} acorns and lose 1 gram of silver.
* Lose b_{X} acorns and gain 1 gram of bronze.
* Gain b_{X} acorns and lose 1 gram of bronze.



Naturally, he cannot perform an operation that would leave him with a negative amount of acorns, gold, silver, or bronze.

What is the maximum number of acorns that he can bring to the nest? Note that gold, silver, or bronze brought to the nest would be worthless because he is just a squirrel.

Constraints

* 1 \leq N \leq 5000
* 1 \leq g_{X} \leq 5000
* 1 \leq s_{X} \leq 5000
* 1 \leq b_{X} \leq 5000
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
g_A s_A b_A
g_B s_B b_B


Output

Print the maximum number of acorns that Chokudai can bring to the nest.

Example

Input

23
1 1 1
2 1 1


Output

46
"""

def maximize_acorns(N, g_A, s_A, b_A, g_B, s_B, b_B):
    # Initialize the dynamic programming array
    dp = [0] * (N + 1)
    
    # List to store profitable trades from A to B
    AB = []
    for (a, b) in zip([g_A, s_A, b_A], [g_B, s_B, b_B]):
        if b > a:
            AB.append((a, b))
    
    # Dynamic programming to maximize acorns after trades from A to B
    for i in range(N + 1):
        for (a, b) in AB:
            if i - a >= 0:
                y = dp[i - a] + b - a
                if y > dp[i]:
                    dp[i] = y
    
    # Update the number of acorns after the first set of trades
    N += dp[N]
    
    # Reinitialize the dynamic programming array for the second set of trades
    dp = [0] * (N + 1)
    
    # List to store profitable trades from B to A
    BA = []
    for (b, a) in zip([g_B, s_B, b_B], [g_A, s_A, b_A]):
        if a > b:
            BA.append((b, a))
    
    # Dynamic programming to maximize acorns after trades from B to A
    for i in range(N + 1):
        for (b, a) in BA:
            if i - b >= 0:
                y = dp[i - b] + a - b
                if y > dp[i]:
                    dp[i] = y
    
    # Return the maximum number of acorns after all trades
    return N + dp[N]