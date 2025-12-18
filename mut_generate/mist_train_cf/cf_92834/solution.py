"""
QUESTION:
Implement a function called `cut_rod` that takes two parameters: `p` and `n`, where `p` is a list representing prices of rods of different lengths and `n` is the desired length of the rod. The function should return the maximum revenue that can be obtained by cutting the rod into different pieces. Ensure the time complexity of your solution is O(n^2) and the space complexity is O(n).
"""

def cut_rod(p, n):
    # Create a list to store the optimal revenue for each rod length
    revenue = [0] * (n + 1)

    for i in range(1, n + 1):
        max_revenue = float('-inf')
        for j in range(1, i + 1):
            max_revenue = max(max_revenue, p[j - 1] + revenue[i - j])
        revenue[i] = max_revenue

    return revenue[n]