"""
QUESTION:
Write a function `ways_to_checkout(max_score)` that determines the number of unique ways a player can checkout with a score less than `max_score` in the game of darts. The function should consider the following scoring possibilities: singles (1-20 points), doubles (2-40 points), triples (3-60 points, excluding the bullseye), and bulls (25 and 50 points). A missed throw is considered 0 points. The function should not differentiate between the order of throws with the same score. The function should return the count of unique combinations that sum to a score less than `max_score`.
"""

def ways_to_checkout(max_score):
    scores = list(range(1, 21)) + [25]
    possibilities = [0] + scores + [2*s for s in scores] + [3*s for s in scores[:20]]

    count = 0
    for i in range(len(possibilities)):
        for j in range(i, len(possibilities)):
            for k in range(j, len(possibilities)):
                if possibilities[i] + possibilities[j] + possibilities[k] < max_score:
                    count += 1

    return count