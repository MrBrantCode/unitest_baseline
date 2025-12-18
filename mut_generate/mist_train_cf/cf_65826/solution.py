"""
QUESTION:
Write a function `lemonadeChange(bills, n, m)` that determines whether it's possible to provide every customer with correct change at a lemonade stand. Each customer pays with either a `$5`, `$10`, or `$20` bill and you must provide the correct change so that the net transaction is that the customer pays $5. You can only hold a maximum of `n` $5 bills and `m` $10 bills. If a customer gives you a bill that would cause you to exceed this limit, return `False`. The function should return `True` if and only if you can provide every customer with correct change. The input `bills` will be a list of integers representing the bills given by the customers. The constraints are `0 <= bills.length <= 10000`, `bills[i]` will be either `5`, `10`, or `20`, and `0 <= n, m <= 10000`.
"""

def lemonadeChange(bills, n, m):
    five, ten = 0, 0
    for bill in bills:
        if bill == 5:
            if five == n:
                return False
            five += 1
        elif bill == 10:
            if five == 0 or ten == m:
                return False
            five -= 1
            ten += 1
        elif bill == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True