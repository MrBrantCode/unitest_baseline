"""
QUESTION:
Implement the `cut_rod` function that takes two inputs: a list `p` where `p[i]` represents the price of a rod of length `i` and an integer `n` representing the desired length of the rod. The function should return the maximum revenue that can be obtained by cutting the rod into different pieces. The solution should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def cut_rod(p, n):
    # Create a list to store the optimal revenue for each rod length
    revenue = [0] * (n + 1)

    for i in range(1, n + 1):
        max_revenue = float('-inf')
        for j in range(1, i + 1):
            max_revenue = max(max_revenue, p[j] + revenue[i - j])
        revenue[i] = max_revenue

    return revenue[n]