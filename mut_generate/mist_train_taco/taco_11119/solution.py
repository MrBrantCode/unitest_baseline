"""
QUESTION:
There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.

You are given money in nominal value of `n` with `1<=n<=1500`.

Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.

Good Luck!!!
"""

def calculate_min_notes(n):
    if n % 10 != 0:
        return -1
    
    denominations = (500, 200, 100, 50, 20, 10)
    count = 0
    
    for denomination in denominations:
        if n == 0:
            break
        notes, n = divmod(n, denomination)
        count += notes
    
    return count