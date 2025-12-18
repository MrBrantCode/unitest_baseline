"""
QUESTION:
Write a function named `calculate_market_price` that takes the following parameters: `dividends_per_share`, `growth_rate`, `risk_free_rate`, `portfolio_returns`, `market_returns`, and `expected_market_return`. This function should return the market price of a portfolio according to the no arbitrage condition using the Capital Asset Pricing Model (CAPM) theory. The market price is determined when the portfolio's expected return equals the risk-free rate plus the portfolio's beta times the market risk premium. Assume that the market price equals the present value of its future cash flows.
"""

import numpy as np

def calculate_market_price(dividends_per_share, growth_rate, risk_free_rate, portfolio_returns, market_returns, expected_market_return):
    """
    Calculate the market price of a portfolio according to the no arbitrage condition using the Capital Asset Pricing Model (CAPM) theory.

    Parameters:
    dividends_per_share (float): The dividends per share of the portfolio.
    growth_rate (float): The growth rate of the portfolio.
    risk_free_rate (float): The risk-free rate.
    portfolio_returns (list or numpy array): The returns of the portfolio.
    market_returns (list or numpy array): The returns of the market.
    expected_market_return (float): The expected return of the market.

    Returns:
    float: The market price of the portfolio.
    """

    # Calculate Beta of the portfolio
    portfolio_returns = np.array(portfolio_returns)
    market_returns = np.array(market_returns)
    covariance = np.cov(portfolio_returns, market_returns)[0, 1]
    variance = np.var(market_returns)
    beta = covariance / variance

    # Calculate the Market Risk Premium
    market_risk_premium = expected_market_return - risk_free_rate

    # Compute the Expected Return of the portfolio
    expected_return = risk_free_rate + beta * market_risk_premium

    # Compute the Market Price of the portfolio
    market_price = dividends_per_share / (expected_return - growth_rate)

    return market_price