"""
QUESTION:
Create a function `estimate_investments` that estimates the amount invested in each stock based on their growth rates and the total interest received. The function should take in the following parameters: a list of growth rates `rates`, the total investment amount `total_investment`, and the target interest `target_interest`. The function should return a list of estimated investments in each stock. The total investment amount should be distributed among the stocks in a way that minimizes the error between the estimated total interest and the target interest.
"""

def estimate_investments(rates, total_investment, target_interest, max_iter=10000, tol=1e-2):
    num_stocks = len(rates)
    
    investments = [total_investment / num_stocks] * num_stocks
    
    for _ in range(max_iter):
        curr_interest = sum(i * r for i, r in zip(investments, rates))
        error = curr_interest - target_interest
        
        if abs(error) <= tol:
            break

        shift_amount = error / max(rates)  
        if error > 0:
            max_yld_idx = rates.index(max(rates))
            investments[max_yld_idx] -= shift_amount
        else:
            min_yld_idx = rates.index(min(rates))
            max_yld_idx = rates.index(max(rates))
            investments[min_yld_idx] += shift_amount
            investments[max_yld_idx] -= shift_amount
    
    return investments