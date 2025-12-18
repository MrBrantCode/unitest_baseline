"""
QUESTION:
You are operating a lemonade stand where each lemonade is priced at $5. Customers are queued up to purchase from you, placing their orders one by one. Each customer will purchase only one lemonade and pay with a $5, $10, or $20 bill. You start with no change in hand and can only hold a maximum of n $5 bills and m $10 bills. Write a function lemonadeChange(bills, n, m) that returns true if and only if you can provide every customer with the correct change.
"""

def lemonadeChange(bills, n, m):
    five = ten = 0
    for i in bills:
        if i == 5:
            if five == n:
                return False
            five += 1
        elif i == 10:
            if not five or ten == m:
                return False
            ten += 1
            five -= 1
        elif i == 20:
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True