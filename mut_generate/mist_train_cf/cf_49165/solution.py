"""
QUESTION:
Define the function `checkRecord(n, allowedExcusedDays)` that takes two parameters, `n` (the length of the attendance record) and `allowedExcusedDays` (the maximum number of excused days), and returns the number of possible attendance records of length `n` that would make a student eligible or ineligible for an attendance award.

Constraints:
- `1 <= n <= 10^5`
- `allowedExcusedDays` is either `None` or `2`. If `None`, ignore the 'E' rule; if `2`, a student can only be marked as 'E' for a maximum of `2` days.

The function should return the total number of eligible attendance records considering the rules for 'A', 'L', 'P', and 'E' (if applicable), modulo `10^9 + 7` to avoid overflow.
"""

def checkRecord(n, allowedExcusedDays):
    MOD = 10**9 + 7

    # Base case: If n is less than or equal to 4, return 4^n
    if n <= 4:
        return pow(4, n, MOD)

    # Initialize dp array
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 4
    dp[2] = 13
    dp[3] = 40

    # If allowedExcusedDays is None, ignore the 'E' rule
    if allowedExcusedDays is None:
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
    # If allowedExcusedDays is 2, a student can only be marked as 'E' for a maximum of 2 days
    else:
        for i in range(4, n + 1):
            dp[i] = (1 + dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

    # Calculate the number of eligible attendance records
    eligible_records = (pow(3, n, MOD) - (dp[n] - dp[n - 3]) % MOD) % MOD

    # If allowedExcusedDays is 2, subtract the number of records with more than 2 'E's
    if allowedExcusedDays == 2:
        eligible_records = (eligible_records - (dp[n] - dp[n - 3] - dp[n - 4] - dp[n - 5]) % MOD) % MOD

    return eligible_records