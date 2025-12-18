"""
QUESTION:
Implement the `calculate_discretionary_accruals` function to compute discretionary accruals using the Jones (1991) model. The function should take in the following parameters: `total_assets`, `change_in_revenue`, `change_in_accounts_receivable`, `property_plant_equipment`, `change_in_current_assets`, `change_in_cash`, `change_in_current_liabilities`, `change_in_debt_included_in_current_liabilities`, and `depreciation_and_amortization`. 

The function should return the discretionary accruals. Assume that the regression coefficients (`alpha1`, `alpha2`, and `alpha3`) are already estimated and provided.
"""

def calculate_discretionary_accruals(total_assets, change_in_revenue, change_in_accounts_receivable, 
                                     property_plant_equipment, change_in_current_assets, change_in_cash, 
                                     change_in_current_liabilities, change_in_debt_included_in_current_liabilities, 
                                     depreciation_and_amortization, alpha1, alpha2, alpha3):
    """
    This function calculates discretionary accruals using the Jones (1991) model.

    Parameters:
    total_assets (float): The total assets of the company.
    change_in_revenue (float): The change in revenue.
    change_in_accounts_receivable (float): The change in accounts receivable.
    property_plant_equipment (float): The property, plant, and equipment.
    change_in_current_assets (float): The change in current assets.
    change_in_cash (float): The change in cash.
    change_in_current_liabilities (float): The change in current liabilities.
    change_in_debt_included_in_current_liabilities (float): The change in debt included in current liabilities.
    depreciation_and_amortization (float): The depreciation and amortization.
    alpha1 (float): The first regression coefficient.
    alpha2 (float): The second regression coefficient.
    alpha3 (float): The third regression coefficient.

    Returns:
    float: The discretionary accruals.
    """
    
    # Calculate total accruals
    total_accruals = (change_in_current_assets - change_in_cash) - (change_in_current_liabilities - change_in_debt_included_in_current_liabilities) - depreciation_and_amortization
    
    # Calculate non-discretionary accruals
    non_discretionary_accruals = alpha1 * (1 / total_assets) + alpha2 * (change_in_revenue - change_in_accounts_receivable) + alpha3 * property_plant_equipment
    
    # Calculate discretionary accruals
    discretionary_accruals = total_accruals - non_discretionary_accruals
    
    return discretionary_accruals