"""
QUESTION:
Write a function `least_changes_to_increasing(arr, limit, subset)` that takes a list of integers `arr`, an integer `limit`, and a list of integers `subset`, and returns the minimum number of changes required to make `arr` an increasing sequence by changing its elements to elements from `subset`, without exceeding the `limit`. If no such sequence is possible, return -1. The function should return the smallest modification within the limit if multiple modifications are possible.
"""

def least_changes_to_increasing(arr, limit, subset):
    # First, sort the subset
    subset.sort()

    # Initialize the dynamic programming table.
    dp = [[0 for _ in range(len(subset))] for _ in range(len(arr))]
    
    # Initialize the first row separately
    for j in range(len(subset)):
        dp[0][j] = 1 if arr[0] != subset[j] else 0

    # Iterate over each element of the array and each integer in subset
    for i in range(1, len(arr)):
        min_previous = dp[i - 1][0]
        for j in range(len(subset)):
            # Maintain running minimum of dp[i-1][k] where 0 <= k <= i.
            if j > 0:
                min_previous = min(min_previous, dp[i - 1][j - 1])

            # dp[i][j] can be derived from either dp[i - 1][j] or min_previous.
            # if the current subset element is greater than array element,
            # we need to change array element so, consider it in dp
            dp[i][j] = dp[i - 1][j] + 1 if subset[j] < arr[i] else min_previous   

    # Add last row to result_list and sort it
    result = dp[-1][:]
    result.sort()

    # Return the minimum element in the resulting list which is less than or equal to limit
    for modification in result:
        if modification <= limit:
            return modification

    return -1 # Not possible