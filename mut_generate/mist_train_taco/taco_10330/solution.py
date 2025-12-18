"""
QUESTION:
This is simplified version of the problem used on the original contest. The original problem seems to have too difiicult solution. The constraints for input data have been reduced.

Polycarp likes to play computer role-playing game «Lizards and Basements». At the moment he is playing it as a magician. At one of the last levels he has to fight the line of archers. The only spell with which he can damage them is a fire ball. If Polycarp hits the i-th archer with his fire ball (they are numbered from left to right), the archer loses a health points. At the same time the spell damages the archers adjacent to the i-th (if any) — they lose b (1 ≤ b < a ≤ 10) health points each.

As the extreme archers (i.e. archers numbered 1 and n) are very far, the fire ball cannot reach them. Polycarp can hit any other archer with his fire ball.

The amount of health points for each archer is known. An archer will be killed when this amount is less than 0. What is the minimum amount of spells Polycarp can use to kill all the enemies?

Polycarp can throw his fire ball into an archer if the latter is already killed.

Input

The first line of the input contains three integers n, a, b (3 ≤ n ≤ 10; 1 ≤ b < a ≤ 10). The second line contains a sequence of n integers — h1, h2, ..., hn (1 ≤ hi ≤ 15), where hi is the amount of health points the i-th archer has.

Output

In the first line print t — the required minimum amount of fire balls.

In the second line print t numbers — indexes of the archers that Polycarp should hit to kill all the archers in t shots. All these numbers should be between 2 and n - 1. Separate numbers with spaces. If there are several solutions, output any of them. Print numbers in any order.

Examples

Input

3 2 1
2 2 2


Output

3
2 2 2 

Input

4 3 1
1 4 1 1


Output

4
2 2 3 3
"""

def minimum_fireballs(n, a, b, health_points):
    # Adjust health points to account for the problem's requirement
    health_points = [hp + 1 for hp in health_points]
    
    # Initialize DP and auxiliary arrays
    dp = [[[-1] * 17 for _ in range(17)] for _ in range(n)]
    num = [[[0] * 17 for _ in range(17)] for _ in range(n)]
    health = [[[0] * 17 for _ in range(17)] for _ in range(n)]
    result = []

    def recursion(i, j, k):
        if i == n - 1:
            return float('inf') if j > 0 else 0
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        dp[i][j][k] = float('inf')
        for s in range(17):
            if j <= s * b:
                bt = s + recursion(i + 1, max(0, health_points[i] - k * b - s * a), s)
                if bt < dp[i][j][k]:
                    dp[i][j][k] = bt
                    num[i][j][k] = s
                    health[i][j][k] = max(0, health_points[i] - k * b - s * a)
        return dp[i][j][k]

    def compute(i, j, k):
        nonlocal result
        if i == n - 1:
            return
        result += [str(i + 1)] * num[i][j][k]
        compute(i + 1, health[i][j][k], num[i][j][k])

    # Handle the first and last archers separately
    while health_points[0] > 0:
        health_points[0] = max(health_points[0] - b, 0)
        health_points[1] = max(health_points[1] - a, 0)
        health_points[2] = max(health_points[2] - b, 0)
        result.append(str(2))

    while health_points[n - 1] > 0:
        health_points[n - 1] = max(health_points[n - 1] - b, 0)
        health_points[n - 2] = max(health_points[n - 2] - a, 0)
        health_points[n - 3] = max(health_points[n - 3] - b, 0)
        result.append(str(n - 1))

    # Compute the minimum fireballs required
    recursion(1, 0, 0)
    compute(1, 0, 0)

    # Return the results
    min_fireballs = len(result)
    fireball_targets = result
    return min_fireballs, fireball_targets