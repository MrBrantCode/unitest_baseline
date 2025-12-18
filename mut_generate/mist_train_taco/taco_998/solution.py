"""
QUESTION:
Takahashi is at an all-you-can-eat restaurant.
The restaurant offers N kinds of dishes. It takes A_i minutes to eat the i-th dish, whose deliciousness is B_i.
The restaurant has the following rules:
 - You can only order one dish at a time. The dish ordered will be immediately served and ready to eat.
 - You cannot order the same kind of dish more than once.
 - Until you finish eating the dish already served, you cannot order a new dish.
 - After T-0.5 minutes from the first order, you can no longer place a new order, but you can continue eating the dish already served.
Let Takahashi's happiness be the sum of the deliciousness of the dishes he eats in this restaurant.
What is the maximum possible happiness achieved by making optimal choices?

-----Constraints-----
 - 2 \leq N \leq 3000
 - 1 \leq T \leq 3000
 - 1 \leq A_i \leq 3000
 - 1 \leq B_i \leq 3000
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N T
A_1 B_1
:
A_N B_N

-----Output-----
Print the maximum possible happiness Takahashi can achieve.

-----Sample Input-----
2 60
10 10
100 100

-----Sample Output-----
110

By ordering the first and second dishes in this order, Takahashi's happiness will be 110.
Note that, if we manage to order a dish in time, we can spend any amount of time to eat it.
"""

import numpy as np

def max_happiness(N, T, dishes):
    # Sort dishes by time to eat (A_i) and then by deliciousness (B_i) in descending order
    dishes.sort(key=lambda x: (x[0], -x[1]))
    
    # Initialize the dp array with zeros, representing the maximum happiness at each time point
    dp = np.array([0] * T)
    
    # Initialize the answer to track the maximum happiness
    ans = 0
    
    # Iterate over each dish
    for (a, b) in dishes:
        # Update the answer with the maximum happiness considering the current dish
        ans = max(ans, dp[-1] + b)
        
        # Update the dp array for times greater than or equal to a
        dp[a:] = np.maximum(dp[:-a] + b, dp[a:])
    
    # The maximum happiness is the maximum value between the last element of dp and ans
    return max(ans, dp[-1])