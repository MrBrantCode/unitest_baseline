"""
QUESTION:
Implement a function `update_learning_rate` that takes a single argument `r2_score` and returns the updated learning rate for an SGDRegressor model based on the following conditions:
- If `r2_score` is greater than 0.9, return 0.001.
- If `r2_score` is less than 0.7, return 0.01.
- Otherwise, return 0.1.

Note that the function should not take any other arguments besides `r2_score`.
"""

def update_learning_rate(r2_score):
    if r2_score > 0.9:
        return 0.001
    elif r2_score < 0.7:
        return 0.01
    else:
        return 0.1