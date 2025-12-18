"""
QUESTION:
There is a street by the name of colorful street in the Pretty Town. The residents of the house have decided that they will paint their houses in either Pink, Orange or Yellow color and not other. They have also decided that no two adjacent houses will have the same color. For house i, i-1 and i+1 are the neighbors and note that the first and the last house are not neighbors.

The cost of painting a house in a particular color is different. The cost of painting the first house in color yellow maybe different than what its for painting the second house in the same color. 

You have to find the minimum of cost of painting the houses which satisfy the given condition.

Input Constraints
 - Number of houses will contain between 1 and 20 elements, inclusive.
 - Each line of input for houses will have three values for cost of coloring in each color. Each value will be between 1 and 1000.

Input Format
- The first line will contain the number of test cases - T.
 - The second line will contain an integer N that will specify how many houses are there.
 - Each of the following N lines will contain 3 numbers separated by space that represents the cost of painting that house in either pink, orange or yellow color.

Output Format
Print T lines showing the cost of painting the houses for each test case.

SAMPLE INPUT
1
2
11 12 13
14 15 16

SAMPLE OUTPUT
26

Explanation

The first house should be painted in pink (11), the second should be painted in orange (15). So the total cost becomes  11+15 = 26
"""

def calculate_minimum_painting_cost(num_houses, costs):
    # Initialize the DP table with the same structure as costs
    dp = [[0] * 3 for _ in range(num_houses)]
    
    # Base case: cost to paint the first house
    dp[0] = costs[0]
    
    # Fill the DP table
    for i in range(1, num_houses):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    # The answer is the minimum cost to paint the last house with any color
    min_cost = min(dp[-1])
    
    return min_cost