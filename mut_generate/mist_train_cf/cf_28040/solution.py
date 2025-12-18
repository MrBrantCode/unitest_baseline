"""
QUESTION:
Implement a function `calculate_ai(a, j, k)` that takes three integers `a`, `j`, and `k` as input and simulates the behavior of the given loop to return the final value of `ai`. In the loop, if `j` equals 0, set `ai` to `a`. Otherwise, find the maximum (`mx`) and minimum (`mi`) digits of `ai`, and if `mi` is not 0, update `ai` by adding the product of `mx` and `mi`. The loop runs until `j` is no longer less than `k`. If the loop does not execute at all, return the initial value of `ai` (which is 0).
"""

def entrance(a, j, k):
    ai = 0
    while j < k:
        if j == 0:
            ai = a
        else:
            mx = 0
            mi = 9
            for i in str(ai):
                mx = max(mx, int(i))
                mi = min(mi, int(i))
            if int(mi) == 0:
                break
            ai += int(mx) * int(mi)
        j += 1
    return ai