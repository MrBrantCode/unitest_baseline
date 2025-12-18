"""
QUESTION:
Given a function `bagOfTokensScore(tokens, P)` where `tokens` is a list of integers representing the values of tokens in a bag and `P` is an integer representing the initial power, return the largest possible score that can be achieved by playing tokens face up or face down, subject to the following rules:
- A token can be played face up if the current power is at least the value of the token, resulting in a loss of power equal to the token's value and a gain of 1 score.
- A token can be played face down if the current score is at least 1, resulting in a gain of power equal to the token's value and a loss of 1 score.
- Each token may be played at most once and in any order.
- A token can only be played face down if it is the highest value token remaining in the bag.
- A token can only be played face up if it is the lowest value token remaining in the bag.
- `0 <= tokens.length <= 1000` and `0 <= tokens[i], P < 10^4`.
"""

def bagOfTokensScore(tokens, P):
    tokens.sort()
    score = 0
    max_score = 0
    while tokens:
        if P >= tokens[0]:
            P -= tokens.pop(0)
            score += 1
            max_score = max(max_score, score)
        elif score > 0 and len(tokens) > 1:
            P += tokens.pop()
            score -= 1
        else:
            break
    return max_score