"""
QUESTION:
Write a function `compute_roi` for the `Business` class. The function should take a list of tuples `period` as input, where each tuple contains the revenue and expenses for a particular time period. The function should return the ROI calculated based on the profit acquired from the assets and the expenses incurred within the specified period. The class should also have an attribute `roi_duration` to store the duration for which the ROI is computed. The computation of ROI should require multiple steps and be well-defined.
"""

def compute_roi(period, assets, expenses):
    # Compute the sum of all revenues for the specified period
    revenue = sum([r for r, p in period])
    
    # Compute the sum of all expenses for the specified period
    expenses_period = sum([p for r, p in period])
    
    # Compute the profit as the difference between revenue and expenses
    profit = revenue - expenses_period
    
    # Compute the ROI using the profit and expenses
    if assets == 0:
        return 0
    
    roi = (profit - expenses) / assets
    
    return roi