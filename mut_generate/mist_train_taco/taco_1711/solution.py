"""
QUESTION:
Small Pizza has an area of 'S' units. Medium Pizza has an area of 'M' units. Large Pizza has an area of 'L' units.
Cost of Small, medium and Large Pizza is 'CS' , 'CM', and 'CL' respectively. What is the minimum amount of money needed so that one can buy atleast X units square of Pizza?
 
Example 1:
Input:
X = 16, S = 3, M = 6, L = 9, CS = 50, CM = 150, CL = 300
Output:
300
Explanation:
We want atleast 16 sq. units of Pizza.
1S 1M 1L area= 3+6+9 = 18 sq units, Cost=500
6S  area=18 sq units, Cost=300
2L area=18 sq units, Cost=600 etc.
Of all the Arrangements, Minimum Cost is Rs. 300.
Example 2:
Input:
X = 10, S = 1, M = 3, L = 10, CS = 10, CM = 20, CL = 50
Output:
50
Explanation:
Of all the Arrangements possible,
Minimum Cost is Rs. 50.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getPizza() which takes 7 Integers X, S, M, L, CS, CM, and CL as input and returns the minimum amount needed to buy atleast X sq. units of Pizza .
 
Expected Time Complexity: O(X)
Expected Auxiliary Space: O(X)
 
Constraints:
1 <= X <= 500
1 <= S <= M <= L <= 100
1 <= CS <= CM <= CL <= 100
"""

def calculate_minimum_pizza_cost(X, S, M, L, CS, CM, CL):
    def rec(i, x, s, m, l, cs, cm, cl, dp):
        if i >= x:
            return 0
        elif dp[i] != -1:
            return dp[i]
        a = rec(i + s, x, s, m, l, cs, cm, cl, dp) + cs
        b = rec(i + m, x, s, m, l, cs, cm, cl, dp) + cm
        c = rec(i + l, x, s, m, l, cs, cm, cl, dp) + cl
        dp[i] = min(a, b, c)
        return dp[i]
    
    dp = [-1] * (2 * X)
    return rec(0, X, S, M, L, CS, CM, CL, dp)