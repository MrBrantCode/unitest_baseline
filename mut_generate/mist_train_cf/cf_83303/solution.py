"""
QUESTION:
Design a function `bagOfTokensScore(tokens, P)` that takes a list of integers `tokens` representing the values of the tokens in the bag and an integer `P` representing the initial power. The function should return the largest possible score that can be achieved after playing any number of tokens.

Restrictions:

- `0 <= tokens.length <= 1000`
- `0 <= tokens[i], P < 104`

Note: The function should consider playing tokens face up or face down, following the given rules: 
- Playing a token face up requires the current power to be at least the token's value and gains 1 score.
- Playing a token face down requires the current score to be at least 1, gains the token's value in power, and loses 1 score.
"""

import collections

def bagOfTokensScore(tokens, P):
    tokens.sort()
    deque = collections.deque(tokens)
    ans = bns = 0
    while deque and (deque[0] <= P or bns):
        while deque and deque[0] <= P:
            P -= deque.popleft()
            bns += 1
        ans = max(ans, bns)

        if deque and bns:
            P += deque.pop()
            bns -= 1

    return ans