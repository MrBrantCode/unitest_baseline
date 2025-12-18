"""
QUESTION:
Write a function `maxScoreSightseeingPair(values)` that takes an integer array `values` as input, where `values[i]` represents the value of the `ith` sightseeing spot. The function should return the maximum score of a pair of sightseeing spots and the indices of the pair that gives the maximum score. The score of a pair (`i &lt; j`) of sightseeing spots is `values[i] + values[j] + i - j`. The constraints are `2 &lt;= values.length &lt;= 5 * 104` and `1 &lt;= values[i] &lt;= 1000`.
"""

def maxScoreSightseeingPair(values):
    max_value = values[0]
    max_score = float('-inf')
    for i in range(1, len(values)):
        max_score = max(max_score, max_value + values[i] - i)
        max_value = max(max_value, values[i] + i)
    return max_score