"""
QUESTION:
Summer is coming! It's time for Iahub and Iahubina to work out, as they both want to look hot at the beach. The gym where they go is a matrix a with n lines and m columns. Let number a[i][j] represents the calories burned by performing workout at the cell of gym in the i-th line and the j-th column.

Iahub starts with workout located at line 1 and column 1. He needs to finish with workout a[n][m]. After finishing workout a[i][j], he can go to workout a[i + 1][j] or a[i][j + 1]. Similarly, Iahubina starts with workout a[n][1] and she needs to finish with workout a[1][m]. After finishing workout from cell a[i][j], she goes to either a[i][j + 1] or a[i - 1][j]. 

There is one additional condition for their training. They have to meet in exactly one cell of gym. At that cell, none of them will work out. They will talk about fast exponentiation (pretty odd small talk) and then both of them will move to the next workout.

If a workout was done by either Iahub or Iahubina, it counts as total gain. Please plan a workout for Iahub and Iahubina such as total gain to be as big as possible. Note, that Iahub and Iahubina can perform workouts with different speed, so the number of cells that they use to reach meet cell may differs.


-----Input-----

The first line of the input contains two integers n and m (3 ≤ n, m ≤ 1000). Each of the next n lines contains m integers: j-th number from i-th line denotes element a[i][j] (0 ≤ a[i][j] ≤ 10^5).


-----Output-----

The output contains a single number — the maximum total gain possible. 


-----Examples-----
Input
3 3
100 100 100
100 1 100
100 100 100

Output
800


-----Note-----

Iahub will choose exercises a[1][1] → a[1][2] → a[2][2] → a[3][2] → a[3][3]. Iahubina will choose exercises a[3][1] → a[2][1] → a[2][2] → a[2][3] → a[1][3].
"""

def calculate_max_total_gain(n, m, gym):
    # Initialize auxiliary matrices for dynamic programming
    bToMid = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    bToEnd = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    aToMid = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    aToEnd = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    
    # Fill bToMid matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            bToMid[i][j] = gym[i - 1][j - 1] + max(bToMid[i - 1][j], bToMid[i][j - 1])
    
    # Fill bToEnd matrix
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            bToEnd[i][j] = gym[i - 1][j - 1] + max(bToEnd[i + 1][j], bToEnd[i][j + 1])
    
    # Fill aToMid matrix
    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            aToMid[i][j] = gym[i - 1][j - 1] + max(aToMid[i + 1][j], aToMid[i][j - 1])
    
    # Fill aToEnd matrix
    for i in range(1, n + 1):
        for j in range(m, 0, -1):
            aToEnd[i][j] = gym[i - 1][j - 1] + max(aToEnd[i - 1][j], aToEnd[i][j + 1])
    
    # Calculate the maximum total gain
    best = 0
    for i in range(2, n):
        for j in range(2, m):
            best = max(best, bToMid[i][j - 1] + bToEnd[i][j + 1] + aToMid[i + 1][j] + aToEnd[i - 1][j])
            best = max(best, bToMid[i - 1][j] + bToEnd[i + 1][j] + aToMid[i][j - 1] + aToEnd[i][j + 1])
    
    return best