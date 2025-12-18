"""
QUESTION:
Implement the `dtw_distance` function to calculate the dynamic time warping (DTW) distance between two given time series `ts1` and `ts2`. The time series are represented as lists of numerical values. The function should take `ts1` and `ts2` as input and return the DTW distance. The DTW distance is calculated using dynamic programming and is defined as the minimum cumulative distance between the two time series, allowing for non-linear alignments.
"""

def dtw_distance(ts1, ts2):
    n = len(ts1)
    m = len(ts2)
    
    # Create a 2D array to store the cumulative distances
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    # Calculate cumulative distances
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(ts1[i - 1] - ts2[j - 1])
            dp[i][j] = cost + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[n][m]