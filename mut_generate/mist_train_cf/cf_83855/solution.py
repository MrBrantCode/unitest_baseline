"""
QUESTION:
You are given a variable `n` representing the number of days. Hercy deposits money into the Leetcode financial institution on a daily basis, starting with `$1` on Monday and increasing by `$1` each day compared to the previous day. On every following Monday, his deposit increases by `$1` compared to the previous Monday. Compute the cumulative sum of money Hercy will have in the Leetcode financial institution at the conclusion of the `nth` day.

The function name should be `totalMoney` and it should take an integer `n` as input and return the cumulative sum. The input `n` is guaranteed to be in the range `1 <= n <= 1000`.
"""

def totalMoney(n: int) -> int:
    weeks = n // 7 
    days = n % 7  

    base = [1,2,3,4,5,6,7]
    total_weeks = sum([sum([base[i] + j for i in range(7)]) for j in range(weeks)])
    
    base = [1+i for i in range(7)]
    remaining_days = sum(base[:days])

    return total_weeks + remaining_days