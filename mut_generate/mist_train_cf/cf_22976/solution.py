"""
QUESTION:
Implement a function `knapsack` that takes in a list of items, where each item is a tuple of its weight and value, and the maximum weight capacity of the knapsack, and returns the maximum value that can be obtained without exceeding the weight capacity. The function should use the Bottom-Up Dynamic Programming approach and optimize the solution using memoization.

Note: The function should not take any additional parameters other than the list of items and the maximum weight capacity.
"""

def knapsack(items, capacity):
    """
    This function implements the 0/1 Knapsack problem using the Bottom-Up Dynamic Programming approach with memoization.
    
    Parameters:
    items (list): A list of items, where each item is a tuple of its weight and value.
    capacity (int): The maximum weight capacity of the knapsack.
    
    Returns:
    int: The maximum value that can be obtained without exceeding the weight capacity.
    """

    n = len(items)
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def knapsackHelper(i, w):
        # Check if the value for the current subproblem at [i][w] is already computed and stored in the memoization table
        if dp[i][w] != -1:
            return dp[i][w]

        # Base case: If the weight of the current item i is greater than the current weight capacity w, return 0
        if i == 0 or w == 0:
            result = 0
        elif items[i-1][0] > w:
            result = 0
        # If the weight of the current item i is less than or equal to the current weight capacity w, consider two options
        else:
            # Include the current item i in the knapsack and recursively call the knapsackHelper function
            include_item = items[i-1][1] + knapsackHelper(i-1, w-items[i-1][0])
            # Do not include the current item i in the knapsack and recursively call the knapsackHelper function
            exclude_item = knapsackHelper(i-1, w)
            # Return the maximum value between the two recursive calls
            result = max(include_item, exclude_item)

        # Store the result in the memoization table at [i][w]
        dp[i][w] = result
        return result

    # Call the knapsackHelper function with the initial parameters (n, capacity)
    return knapsackHelper(n, capacity)