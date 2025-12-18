"""
QUESTION:
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 
 
Example 1:
Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 
Example 2:
Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.
 
Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size n and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.
Expected Time Complexity : O(NlogN)
Expected Auxilliary Space: O(1)
Constraints:
1 <= N <= 10^{5}
1 <= W <= 10^{5}
"""

def fractional_knapsack(W: int, values: list, weights: list, n: int) -> float:
    # Create a list of items with their value and weight
    items = [Item(values[i], weights[i]) for i in range(n)]
    
    # Sort items based on value per unit weight in descending order
    items.sort(key=lambda x: -1 * (x.value / x.weight))
    
    profit = 0.0
    for item in items:
        if item.weight <= W:
            W -= item.weight
            profit += item.value
        else:
            profit += W * (item.value / item.weight)
            break
    
    return profit

# Define the Item class
class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w