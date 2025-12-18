"""
QUESTION:
Create a function named `stable_flight` that takes in three parameters: `q` (a list of integers), `w` (the maximum allowable weight), and `k` (the limit for each element). The function should return `True` if `q` can achieve stable flight and `False` otherwise. To achieve stable flight, `q` must meet three conditions: being palindromic, having its components' sum ≤ `w`, and no single element of the list being greater than `k`.
"""

def stable_flight(q, w, k):
    return q == q[::-1] and sum(q) <= w and all(i <= k for i in q)