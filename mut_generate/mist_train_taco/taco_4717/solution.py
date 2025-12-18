"""
QUESTION:
Simple interest on a loan is calculated by simply taking the initial amount (the principal, p) and multiplying it by a rate of interest (r) and the number of time periods (n). 

Compound interest is calculated by adding the interest after each time period to the amount owed, then calculating the next interest payment based on the principal PLUS the interest from all previous periods.

Given a principal *p*, interest rate *r*, and a number of periods *n*, return an array [total owed under simple interest, total owed under compound interest]. 

```
EXAMPLES:

interest(100,0.1,1) = [110,110]
interest(100,0.1,2) = [120,121]
interest(100,0.1,10) = [200,259]
```
 
Round all answers to the nearest integer. Principal will always be an integer between 0 and 9999; interest rate will be a decimal between 0 and 1; number of time periods will be an integer between 0 and 49. 
 
---

More on [Simple interest, compound interest and continuous interest](https://betterexplained.com/articles/a-visual-guide-to-simple-compound-and-continuous-interest-rates/)
"""

def calculate_interest(principal, interest_rate, periods):
    """
    Calculate the total amount owed under simple and compound interest.

    Parameters:
    principal (float or int): The initial amount (principal) of the loan.
    interest_rate (float): The rate of interest, expressed as a decimal.
    periods (int): The number of time periods over which the interest is calculated.

    Returns:
    list: A list containing two integers:
          1. The total amount owed under simple interest.
          2. The total amount owed under compound interest.
    """
    simple_interest = principal * (1 + interest_rate * periods)
    compound_interest = principal * (1 + interest_rate) ** periods
    
    return [round(simple_interest), round(compound_interest)]