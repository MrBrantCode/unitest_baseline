"""
QUESTION:
When Kefa came to the restaurant and sat at a table, the waiter immediately brought him the menu. There were n dishes. Kefa knows that he needs exactly m dishes. But at that, he doesn't want to order the same dish twice to taste as many dishes as possible. 

Kefa knows that the i-th dish gives him ai units of satisfaction. But some dishes do not go well together and some dishes go very well together. Kefa set to himself k rules of eating food of the following type — if he eats dish x exactly before dish y (there should be no other dishes between x and y), then his satisfaction level raises by c. 

Of course, our parrot wants to get some maximal possible satisfaction from going to the restaurant. Help him in this hard task!

Input

The first line of the input contains three space-separated numbers, n, m and k (1 ≤ m ≤ n ≤ 18, 0 ≤ k ≤ n * (n - 1)) — the number of dishes on the menu, the number of portions Kefa needs to eat to get full and the number of eating rules.

The second line contains n space-separated numbers ai, (0 ≤ ai ≤ 109) — the satisfaction he gets from the i-th dish.

Next k lines contain the rules. The i-th rule is described by the three numbers xi, yi and ci (1 ≤ xi, yi ≤ n, 0 ≤ ci ≤ 109). That means that if you eat dish xi right before dish yi, then the Kefa's satisfaction increases by ci. It is guaranteed that there are no such pairs of indexes i and j (1 ≤ i < j ≤ k), that xi = xj and yi = yj.

Output

In the single line of the output print the maximum satisfaction that Kefa can get from going to the restaurant.

Examples

Input

2 2 1
1 1
2 1 1


Output

3


Input

4 3 2
1 2 3 4
2 1 5
3 4 2


Output

12

Note

In the first sample it is best to first eat the second dish, then the first one. Then we get one unit of satisfaction for each dish and plus one more for the rule.

In the second test the fitting sequences of choice are 4 2 1 or 2 1 4. In both cases we get satisfaction 7 for dishes and also, if we fulfill rule 1, we get an additional satisfaction 5.
"""

def calculate_max_satisfaction(n, m, k, satisfaction, rules):
    # Initialize the tree matrix
    tree = [[0] * n for _ in range(n)]
    for (x, y, z) in rules:
        tree[x - 1][y - 1] = float(z)
    
    # Calculate the power of 2 array
    po = [1]
    while len(po) != n:
        po.append(po[-1] * 2)
    
    # Initialize the dp array
    dp = [[0] * (po[-1] * 2) for _ in range(n)]
    for i in range(n):
        dp[i][po[i]] = satisfaction[i]
    
    # Fill the dp array
    for i in range(po[-1] * 2):
        for j in range(n):
            if i & po[j]:
                for k in range(n):
                    if not i & po[k]:
                        dp[k][i + po[k]] = max(dp[k][i + po[k]], dp[j][i] + satisfaction[k] + tree[j][k])
    
    # Find the maximum satisfaction
    ma = 0
    for i in range(po[-1] * 2):
        if bin(i)[2:].count('1') == m:
            for j in range(n):
                ma = max(ma, dp[j][i])
    
    return int(ma)