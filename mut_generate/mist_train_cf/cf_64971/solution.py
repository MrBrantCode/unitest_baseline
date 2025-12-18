"""
QUESTION:
Design a function `bagOfTokensScore` that takes a sorted list of token values `tokens` and an integer `P` as input, and returns the maximum possible score that can be achieved by playing the tokens. The function should follow these rules:
- `tokens[i]` is the value of the `ith` token.
- The function starts with an initial power of `P` and an initial score of `0`.
- A token can be played face up if the current power is at least the token's value, losing the token's value in power and gaining `1` in score.
- A token can be played face down if the current score is at least `1`, gaining the token's value in power and losing `1` in score.
- A token can only be played once.
- A token can only be played face down if it is the highest value token remaining.
- A token can only be played face up if it is the lowest value token remaining.
- A token can only be played face down if the current score is an even number.
- A token can only be played face up if the current power is a multiple of `5`.
The input is restricted to `0 <= tokens.length <= 1000`, `0 <= tokens[i], P <= 104`, and `P` is a multiple of `5`.
"""

def bagOfTokensScore(tokens, P):
    # Sort tokens
    tokens.sort()
    
    # Initialize two pointers at both ends
    l, r = 0, len(tokens) - 1
    
    # Initialize score
    score = 0
    
    # Iterate while left pointer is not more than right
    while l <= r:
        # If power is sufficient to play token face up, go for it
        if P >= tokens[l]:
            P -= tokens[l]
            score += 1
            l += 1
            
        # If not able to play token face up, and can play token face down, play face down
        elif score > 0 and P < tokens[r]:
            P += tokens[r]
            score -= 1
            r -= 1
            
        # If no option left, break
        else:
            break
            
    return score