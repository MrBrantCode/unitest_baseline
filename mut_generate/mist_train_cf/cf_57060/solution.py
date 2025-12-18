"""
QUESTION:
Create a function called `calculate_kpi` that takes in the following parameters: `loan_size`, `apr`, `tenor`, and `ppp`. The function should calculate a KPI based on the disbursement of loans by the sales team, taking into account the size of the loan, the tenor or term of the loan, and the APR of the loan. The KPI should be tailored to different regions by incorporating purchasing power parity (PPP) of a country. Assume the PPP value is given for each country.

The function should return the calculated KPI value.
"""

def calculate_kpi(loan_size, apr, tenor, ppp):
    """
    Calculates the KPI based on loan disbursement by the sales team, 
    considering loan size, tenor, APR, and purchasing power parity (PPP).
    
    Parameters:
    loan_size (float): The size of the loan.
    apr (float): The APR of the loan.
    tenor (float): The term of the loan.
    ppp (float): The purchasing power parity of a country.
    
    Returns:
    float: The calculated KPI value.
    """
    # Calculate the profitability index
    profitability_index = loan_size * apr * tenor
    
    # Calculate the PPP adjusted profitability index
    ppp_adjusted_profitability_index = profitability_index / ppp
    
    return ppp_adjusted_profitability_index