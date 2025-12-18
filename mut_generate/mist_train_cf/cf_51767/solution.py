"""
QUESTION:
Create a function called `total_window_repair_cost` that calculates the total cost to repair multiple windows. The function should take four parameters: `timber_cost_per_foot`, `timber_needed_per_window`, `glass_cost_per_panel`, `glass_panels_needed_per_window`, and `total_windows`. The function should return the total cost of materials needed to repair all windows.
"""

def total_window_repair_cost(timber_cost_per_foot, timber_needed_per_window, glass_cost_per_panel, glass_panels_needed_per_window, total_windows):
    """
    Calculate the total cost to repair multiple windows.

    Parameters:
    timber_cost_per_foot (float): The cost of timber per foot.
    timber_needed_per_window (int): The amount of timber needed per window.
    glass_cost_per_panel (float): The cost of glass per panel.
    glass_panels_needed_per_window (int): The number of glass panels needed per window.
    total_windows (int): The total number of windows.

    Returns:
    float: The total cost of materials needed to repair all windows.
    """
    timber_cost_for_one_window = timber_cost_per_foot * timber_needed_per_window
    glass_cost_for_one_window = glass_cost_per_panel * glass_panels_needed_per_window
    total_cost_for_one_window = timber_cost_for_one_window + glass_cost_for_one_window
    total_cost_for_all_windows = total_cost_for_one_window * total_windows
    return total_cost_for_all_windows