"""
QUESTION:
Create a function named `jobScheduling` that takes three arrays of integers as input: `startTime`, `endTime`, and `profit`, where `startTime[i]`, `endTime[i]`, and `profit[i]` represent the start time, end time, and profit of the `i-th` job, respectively. The function should return the maximum possible profit that can be achieved by selecting a subset of non-overlapping jobs.

The function is subject to the following constraints:
- `1 <= len(startTime) == len(endTime) == len(profit) <= 5 * 10^4`
- `1 <= startTime[i] < endTime[i] <= 10^9`
- `1 <= profit[i] <= 10^4`
"""

def jobScheduling(startTime, endTime, profit):
    # Prepare a list of jobs
    jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    N = len(jobs)
    dp = [0] * (N + 1)
    # Used to store the maximum value of profit
    for i in range(1, N + 1):
        # Update the dp[i] value
        dp[i] = max(jobs[i-1][2] + (dp[i-2] if i-2 >= 0 else 0), dp[i-1])
        
    # Return the final value
    return dp[-1]