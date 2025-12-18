"""
QUESTION:
You are given three inputs: `customers`, `grumpy`, and `X`, where `customers` and `grumpy` are lists of the same length and `X` is an integer. `customers[i]` represents the number of customers that enter the shop at minute `i` and `grumpy[i]` is `1` if the shop owner is grumpy at minute `i` and `0` otherwise. The shop owner can use a secret technique to not be grumpy for `X` minutes straight. Return the maximum number of customers that can be satisfied throughout the day.

Restrictions: `1 <= X < len(customers) == len(grumpy) <= 25000`, `0 <= customers[i] <= 1500`, and `0 <= grumpy[i] <= 1`. 

Implement the function `maxSatisfied(customers, grumpy, X)` to find the maximum number of customers that can be satisfied throughout the day.
"""

def maxSatisfied(customers, grumpy, X):
    n = len(customers)
    curr_sum = max_sum = sum(customers[i] * grumpy[i] for i in range(X))  
    prefix_sum = [0] * n
    prefix_sum[0] = customers[0] * (1 - grumpy[0])

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + customers[i] * (1 - grumpy[i])
        if i >= X:
            curr_sum -= customers[i - X] * grumpy[i - X]  
        curr_sum += customers[i] * grumpy[i]  
        max_sum = max(max_sum, curr_sum)

    return prefix_sum[n - 1] + max_sum if n > X else max_sum