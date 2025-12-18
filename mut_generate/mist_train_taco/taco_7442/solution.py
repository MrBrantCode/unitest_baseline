"""
QUESTION:
Alice plays the following game, loosely based on the card game "21".
Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.
Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?
Example 1:
Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.

Example 2:
Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.

Example 3:
Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
"""

def calculate_probability_of_points(N: int, K: int, W: int) -> float:
    dp = [0] * (N + W + 1)
    for i in range(K, N + 1):
        dp[i] = 1
    S = min(W, N - K + 1)
    for i in range(K - 1, -1, -1):
        dp[i] = S / W
        S += dp[i] - dp[i + W]
    return dp[0]