"""
QUESTION:
Write a function called `interest_calc` that takes two parameters: `total_deposits` and `total_interest`. The function should calculate and return the amount of money in each of three account types (A, B, C) given the following conditions:

- The interest rates for the accounts are: A (7% p.a.), B (9% p.a.), and C (5% p.a.).
- The allowed percentages of total deposits for each account type are: A (10% or 50%), B (30% or 60%), and C (the remaining amount).
- The function should test all possible combinations of account types and percentages to find the amounts that result in the given total deposits and total interest.
"""

def interest_calc(total_deposits, total_interest):
    rates = {'A':0.07,'B':0.09,'C':0.05}
    pcts = {'A':[10,50],'B':[30,60],'C':[40,90]}

    for pctA in pcts['A']:
        for pctB in pcts['B']:
            for pctC in pcts['C']:
                totalA = total_deposits * pctA / 100
                totalB = total_deposits * pctB / 100
                totalC = total_deposits * pctC / 100
                if totalA + totalB + totalC == total_deposits:
                    interestA = totalA * rates['A']
                    interestB = totalB * rates['B']
                    interestC = totalC * rates['C']
                    if interestA + interestB + interestC == total_interest:
                        return {'A': totalA, 'B': totalB, 'C': totalC}