"""
QUESTION:
Given an integer array `score` of size `n`, where `score[i]` is the score of the `ith` athlete in a competition, and an integer array `performance` of size `n`, where `performance[i]` is the performance score of the `ith` athlete, return an array `finalScore` of size `n` where `finalScore[i]` is the final score of the `ith` athlete. The final score is calculated as the athlete's rank multiplied by their performance score. The rank is determined by the athlete's score, with the highest score receiving the rank "1" (or "Gold Medal"), the second highest score receiving the rank "2" (or "Silver Medal"), the third highest score receiving the rank "3" (or "Bronze Medal"), and so on. In case of a tie, athletes with the same score receive the same rank, and the next athlete(s) receive the next immediate rank. 

Constraints: `n == score.length == performance.length`, `1 <= n <= 10^4`, `0 <= score[i] <= 10^6`, and `1 <= performance[i] <= 10^6`. The function should be named `findRanksAndPerformance`.
"""

def findRanksAndPerformance(score, performance):
    athletes = sorted([(s, idx) for idx, s in enumerate(score)], reverse=True)
    ranks = [0] * len(score)
    finalScore = [0] * len(score)
    prev_score, rank = athletes[0][0], 1
    rank_start = 0

    for idx, (s, orig_idx) in enumerate(athletes):
        if s != prev_score:
            rank = idx + 1
            rank_start = idx
        ranks[orig_idx] = rank
        finalScore[orig_idx] = rank * performance[orig_idx]
        prev_score = s

    return finalScore