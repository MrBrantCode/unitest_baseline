"""
QUESTION:
You are given an array of unique soldier ratings and need to form teams of 3 soldiers where either the rating increases or decreases from left to right. Return the number of valid teams that can be formed and the maximum possible sum of ratings for a valid team.

Function name: `numTeams`
Input: A list of integers `rating` representing the ratings of soldiers, where `3 <= len(rating) <= 1000` and `1 <= rating[i] <= 10^5`. All integers in `rating` are unique.
Output: A tuple containing two integers - the number of valid teams and the maximum possible sum of ratings for a valid team.
Restriction: The function should have a time complexity better than O(n^3) due to the large input size.
"""

def numTeams(rating):
    n = len(rating)
    count, maxSum = 0, 0
    for i in range(1, n - 1):
        smallerBefore, largerBefore = sum(1 for j in range(i) if rating[j] < rating[i]), sum(1 for j in range(i) if rating[j] > rating[i])
        smallerAfter, largerAfter = sum(1 for j in range(i + 1, n) if rating[j] < rating[i]), sum(1 for j in range(i + 1, n) if rating[j] > rating[i])
        count += smallerBefore * largerAfter + largerBefore * smallerAfter
        maxSum = max(maxSum, rating[i] + max(rating[:i]) + max(rating[i+1:]) if smallerBefore and largerAfter else maxSum)
        maxSum = max(maxSum, rating[i] + max(rating[:i]) + min(rating[i+1:]) if largerBefore and smallerAfter else maxSum)
    return (count, maxSum)