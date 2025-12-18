"""
QUESTION:
Write a function `interpret_ff3_regression_results` that takes in the results of a Fama-French 3-factor (FF3) regression model. The function should interpret the results of the regression, specifically the alpha, beta coefficients, and adjusted R-squared value. The function should be able to handle results from a regression model that includes the Mkt-RF, SMB, and HML factors.
"""

def interpret_ff3_regression_results(results):
    """
    Interpret the results of a Fama-French 3-factor regression model.

    Parameters:
    results (dict): Dictionary containing the results of the regression model.
                    It should have the following keys:
                    - 'alpha': Alpha coefficient
                    - 'beta1' or 'Mkt-RF': Beta coefficient for the market risk factor
                    - 'beta2' or 'SMB': Beta coefficient for the size factor
                    - 'beta3' or 'HML': Beta coefficient for the value factor
                    - 'adj_r_squared' or 'adjusted R-squared': Adjusted R-squared value

    Returns:
    A string with the interpretation of the results.
    """

    alpha = results.get('alpha')
    beta1 = results.get('beta1') or results.get('Mkt-RF')
    beta2 = results.get('beta2') or results.get('SMB')
    beta3 = results.get('beta3') or results.get('HML')
    adj_r_squared = results.get('adj_r_squared') or results.get('adjusted R-squared')

    interpretation = f"Alpha: {alpha}\n"
    interpretation += f"Alpha close to zero suggests your model does not have any abnormal return over or under the given benchmark (Mkt-RF here).\n\n"

    interpretation += f"Beta1 (MKT-RF): {beta1}\n"
    interpretation += f"Beta1 value of {beta1} implies that for a 1% increase in return of the market portfolio, we expect the portfolio's return (minus the risk-free rate) to increase by {beta1}%.\n\n"

    interpretation += f"Beta2 (SMB): {beta2}\n"
    interpretation += f"Beta2 is a measure of the sensitivity of the stock's returns to the returns of small-minus-big stocks. A positive value ({beta2}) means that your portfolio is prone to perform better in circumstances when small stocks outperform big stocks.\n\n"

    interpretation += f"Beta3 (HML): {beta3}\n"
    interpretation += f"Beta3 is a measure of the sensitivity of the stock's returns to the returns of high book-to-market stocks minus the returns of low book-to-market stocks. A negative value ({beta3}) means that your portfolio tends to perform better when growth stocks (stocks with low book-to-market ratio) outperform value stocks (stocks with high book-to-market ratio).\n\n"

    interpretation += f"Adjusted R^2: {adj_r_squared}\n"
    interpretation += f"An adjusted R^2 of {adj_r_squared} indicates that your chosen factors (Mkt-RF, SMB, HML) explain {adj_r_squared*100}% of the variation in your portfolio or stock's returns."

    return interpretation