"""
QUESTION:
Find the values of four types of shares with annual dividend returns of 3%, 5%, 7%, and 9%, given a total portfolio value of $10,000 and a total dividend return of $600. The function `find_shares(total_value, dividend_returns)` should return the value of each type of share in whole dollars, assuming all values can be represented as multiples of $100.
"""

def find_shares(total_value, dividend_returns):
    for A in range(total_value // 100 + 1):  
        for B in range(total_value // 100 + 1):  
            for C in range(total_value // 100 + 1):  
                D = total_value // 100 - A - B - C  
                if D >= 0 and A * 3 + B * 5 + C * 7 + D * 9 == dividend_returns:
                    return A * 100, B * 100, C * 100, D * 100  
    return None  