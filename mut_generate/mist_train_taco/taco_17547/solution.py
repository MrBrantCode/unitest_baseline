"""
QUESTION:
There is a stack of water glasses in a form of pascal triangle and a person wants to pour the water at the topmost glass, but the capacity of each glass is 1 unit. Overflow takes place in such a way that after 1 unit, 1/2 of remaining unit gets into bottom left glass and other half in bottom right glass.Now John pours K units of water in the topmost glass and wants to know how much water is there in the Cth glass of the Rth row.
Note: Assume that there are enough glasses in the triangle till no glass overflows.
 
Example 1:
Input:
K = 3, R = 2, C = 1
Output:
1.000000
Explanation:
After the first glass, 2 units of water
will remain and they will spread equally
on the two glasses on the second row.
Therefore, the glass on the 2nd row and
1st column will have 1 unit of water.
Example 2:
Input:
K = 3, R = 2, C = 2
Output:
1.000000
Explanation:
After the first glass, 2 units of water
will remain and they will spread equally
on the two glasses on the second row.
Therefore, the glass on the 2nd row and
2nd column will have 1 unit of water.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function waterOverflow() which takes 3 Integers K, R and C as input and returns the amount of water(6 digits of precision) in the Cth glass of Rth row.
 
Expected Time Complexity: O(K^{2})
Expected Auxiliary Space: O(K^{2})
 
Constraints:
1 <= K <= 500
1 <= R,C <= K
"""

def water_overflow(K, R, C):
    # Initialize a 2D list to represent the glasses
    dp = [[0 for j in range(K + 1)] for i in range(K + 1)]
    
    # Pour the initial amount of water into the topmost glass
    dp[0][0] = K
    
    # Iterate over each row and column to distribute the water
    for i in range(K):
        for j in range(i + 1):
            if dp[i][j] > 1.0:
                rem = dp[i][j] - 1.0
                dp[i][j] = 1.0
                dp[i + 1][j] += rem / 2.0
                dp[i + 1][j + 1] += rem / 2.0
    
    # Return the amount of water in the specified glass with 6 digits of precision
    return '{:.6f}'.format(dp[R - 1][C - 1])