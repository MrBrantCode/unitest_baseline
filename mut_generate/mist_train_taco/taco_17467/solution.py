"""
QUESTION:
After several latest reforms many tourists are planning to visit Berland, and Berland people understood that it's an opportunity to earn money and changed their jobs to attract tourists. Petya, for example, left the IT corporation he had been working for and started to sell souvenirs at the market.

This morning, as usual, Petya will come to the market. Petya has n different souvenirs to sell; ith souvenir is characterised by its weight w_{i} and cost c_{i}. Petya knows that he might not be able to carry all the souvenirs to the market. So Petya wants to choose a subset of souvenirs such that its total weight is not greater than m, and total cost is maximum possible.

Help Petya to determine maximum possible total cost.


-----Input-----

The first line contains two integers n and m (1 ≤ n ≤ 100000, 1 ≤ m ≤ 300000) — the number of Petya's souvenirs and total weight that he can carry to the market.

Then n lines follow. ith line contains two integers w_{i} and c_{i} (1 ≤ w_{i} ≤ 3, 1 ≤ c_{i} ≤ 10^9) — the weight and the cost of ith souvenir.


-----Output-----

Print one number — maximum possible total cost of souvenirs that Petya can carry to the market.


-----Examples-----
Input
1 1
2 1

Output
0

Input
2 2
1 3
2 2

Output
3

Input
4 3
3 10
2 7
2 8
1 1

Output
10
"""

def max_souvenir_cost(n, m, souvenirs):
    # Initialize a list to store the maximum cost for each weight from 0 to m
    dp = [(0, 0, 0) for _ in range(m + 3)]
    
    # Group souvenirs by their weight (1, 2, or 3)
    gp = [[] for _ in range(4)]
    for w, c in souvenirs:
        gp[w].append(c)
    
    # Sort each group in descending order of cost
    for i in range(1, 4):
        gp[i].sort(reverse=True)
    
    # Dynamic programming to find the maximum cost for each weight
    for i in range(m + 1):
        one = dp[i][1]
        two = dp[i][2]
        if one < len(gp[1]):
            if dp[i + 1][0] < dp[i][0] + gp[1][one]:
                dp[i + 1] = (dp[i][0] + gp[1][one], one + 1, two)
        if two < len(gp[2]):
            dp[i + 2] = (dp[i][0] + gp[2][two], one, two + 1)
    
    # Update dp array to ensure each entry is the maximum cost up to that weight
    for i in range(1, m + 1):
        dp[i] = max(dp[i - 1], dp[i])
    
    # Calculate the final answer by considering the maximum cost including weight 3 souvenirs
    ans = dp[m][0]
    tot = 0
    for i in range(len(gp[3]) + 1):
        if 3 * i <= m:
            ans = max(dp[m - 3 * i][0] + tot, ans)
            if i < len(gp[3]):
                tot += gp[3][i]
    
    return ans