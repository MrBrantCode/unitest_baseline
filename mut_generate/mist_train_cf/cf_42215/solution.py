"""
QUESTION:
Implement a function `calculate_health_score` that calculates a health score based on three input parameters: HbA1c level, systolic blood pressure (SBP), and total cholesterol to HDL cholesterol ratio (TCHDL). The function should clean the input values using the following formulas: HbA1c - 6.72, (SBP - 135.7) / 10, and log(TCHDL) - 1.59. The health score should then be calculated using the formula: 1 - exp(-Q * D^ageDiab * (1 - D^tYear) / (1 - D)), where Q is the product of 0.5 and the exponential of 1.2 times the cleaned input values, D is 0.9, ageDiab is 5, and tYear is 10. The function should return the maximum of the calculated health score and 0.0.
"""

import numpy as np

def calculate_health_score(hba1c, sbp, tchdl):
    # Clean the input values
    hba1c_cleaned = hba1c - 6.72
    sbp_cleaned = (sbp - 135.7) / 10
    tchdl_cleaned = np.log(tchdl) - 1.59

    # Define constants
    Q_0 = 0.5
    BETA = 1.2
    D = 0.9
    ageDiab = 5
    tYear = 10

    # Calculate the health score
    xFeat = np.array([hba1c_cleaned, sbp_cleaned, tchdl_cleaned])
    q = Q_0 * np.prod(np.power(BETA, xFeat))
    uscore = 1 - np.exp(-q * D**(ageDiab) * (1 - D**tYear) / (1 - D))
    return max(uscore, 0.0)