"""
QUESTION:
Create a function named `drawdown_contribution` that estimates the contribution of each portfolio to the total drawdown of a multi-portfolio investment. The function should take a list of time-series returns for each portfolio as input, and return the relative contribution of each portfolio to the total drawdown. Note that the function will provide an approximation, as drawdown is not additively decomposable.
"""

def drawdown_contribution(returns):
    # Calculate the drawdown for each portfolio separately
    portfolio_drawdowns = []
    for portfolio in returns:
        peak = 1
        trough = 1
        drawdown = 0
        max_drawdown = 0
        for ret in portfolio:
            peak = peak * (1 + ret)
            trough = min(trough * (1 + ret), peak)
            drawdown = 1 - (trough / peak)
            max_drawdown = max(max_drawdown, drawdown)
        portfolio_drawdowns.append(max_drawdown)

    # Calculate the total drawdown
    total_peak = 1
    total_trough = 1
    total_drawdown = 0
    max_total_drawdown = 0
    for rets in zip(*returns):
        total_peak = total_peak * (1 + sum(rets))
        total_trough = min(total_trough * (1 + sum(rets)), total_peak)
        total_drawdown = 1 - (total_trough / total_peak)
        max_total_drawdown = max(max_total_drawdown, total_drawdown)

    # Estimate the relative contribution of each portfolio to the total drawdown
    contributions = []
    for portfolio_drawdown in portfolio_drawdowns:
        contribution = portfolio_drawdown / max_total_drawdown if max_total_drawdown != 0 else 0
        contributions.append(contribution)

    return contributions