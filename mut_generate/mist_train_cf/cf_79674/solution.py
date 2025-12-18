"""
QUESTION:
Write a function `portfolio_diversity(funds, portfolio, years, return_)` that calculates the possible combinations of investments in each fund type given a list of annual dividend yields `funds`, a total invested amount `portfolio`, an investment period `years`, and a total return `return_`. The function should consider the following restrictions:

- The invested amounts are in multiples of $100.
- No fund has less than $500 investment.
- The interest in the funds is compounded yearly and reinvested back into the portfolios.

The function should return a list of possible combinations of investments in each fund type that result in the total return.
"""

from itertools import product

def portfolio_diversity(funds, portfolio, years, return_):
    rates = [fund / 100. for fund in funds]
    token_sum = portfolio // 100
    solutions = []
    for combination in product(range(5, token_sum+1), repeat=len(funds)):
        if sum(combination) == token_sum:
            sums = [100*token for token in combination]
            return_calculated = sum(summ * (1 + rate / 100) ** years for rate, summ in zip(rates, sums)) - sum(sums)
            if abs(return_calculated - return_) < 1e-2:  # introducing permissible error
                solutions.append(list(zip(funds, sums)))
    return solutions