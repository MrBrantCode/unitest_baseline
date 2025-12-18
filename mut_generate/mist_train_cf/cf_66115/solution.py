"""
QUESTION:
Create a function named 'compound_interest' that takes four parameters: 'principle', 'rate', 'time', and 'comp_freq'. 'principle' is the principal amount, 'rate' is the annual interest rate as a percentage, 'time' is the time period in years, and 'comp_freq' is the number of times interest is compounded per time period. The function should return the compound interest using the formula A = P(1 + r/n)^(nt). 

Ensure the function handles potential errors that may arise from the input values and returns an error message if the inputs are not positive numbers or cannot be converted to numbers. 

The function should be called with user inputs for 'principle', 'rate', 'time', and 'comp_freq', which should be taken as input from the user. The compound interest should be printed out with a friendly message, formatted to two decimal places.
"""

def compound_interest(principle, rate, time, comp_freq):
    try:
        principle = float(principle)
        rate = float(rate)
        time = float(time)
        comp_freq = float(comp_freq)
    except ValueError:
        return "Error: All inputs must be numbers"
    
    if principle < 0 or rate < 0 or time < 0 or comp_freq < 0:
        return "Error: All inputs must be positive numbers"
   
    # Compound interest formula
    amount = principle * pow((1 + rate / (100 * comp_freq)), (comp_freq * time))
    return amount