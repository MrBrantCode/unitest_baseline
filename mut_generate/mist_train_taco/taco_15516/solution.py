"""
QUESTION:
You have a knapsack with the capacity of W. There are also n items, the i-th one has weight w_i. 

You want to put some of these items into the knapsack in such a way that their total weight C is at least half of its size, but (obviously) does not exceed it. Formally, C should satisfy: ⌈ W/2⌉ ≤ C ≤ W. 

Output the list of items you will put into the knapsack or determine that fulfilling the conditions is impossible. 

If there are several possible lists of items satisfying the conditions, you can output any. Note that you don't have to maximize the sum of weights of items in the knapsack.

Input

Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). Description of the test cases follows.

The first line of each test case contains integers n and W (1 ≤ n ≤ 200 000, 1≤ W ≤ 10^{18}). 

The second line of each test case contains n integers w_1, w_2, ..., w_n (1 ≤ w_i ≤ 10^9) — weights of the items.

The sum of n over all test cases does not exceed 200 000.

Output

For each test case, if there is no solution, print a single integer -1. 

If there exists a solution consisting of m items, print m in the first line of the output and m integers j_1, j_2, ..., j_m (1 ≤ j_i ≤ n, all j_i are distinct) in the second line of the output — indices of the items you would like to pack into the knapsack.

If there are several possible lists of items satisfying the conditions, you can output any. Note that you don't have to maximize the sum of weights items in the knapsack.

Example

Input


3
1 3
3
6 2
19 8 19 69 9 4
7 12
1 1 1 17 1 1 1


Output


1
1
-1
6
1 2 3 5 6 7

Note

In the first test case, you can take the item of weight 3 and fill the knapsack just right.

In the second test case, all the items are larger than the knapsack's capacity. Therefore, the answer is -1.

In the third test case, you fill the knapsack exactly in half.
"""

def find_knapsack_items(n, W, weights):
    # Calculate the lower bound for the sum of weights
    lower_bound = (W + 1) // 2
    
    # Create a list of tuples with (weight, index)
    items = [(weights[i], i + 1) for i in range(n)]
    
    # Sort items by weight in descending order
    items.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize variables
    selected_items = []
    current_sum = 0
    
    # Try to select items
    for weight, index in items:
        if weight <= W:
            current_sum += weight
            selected_items.append(index)
            if lower_bound <= current_sum <= W:
                return len(selected_items), selected_items
    
    # If no valid solution is found
    return -1