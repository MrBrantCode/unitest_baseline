"""
QUESTION:
Write a Python function called `calculate_lease_options` that takes four parameters: `monthly_expenses`, `one_year_lease`, `two_year_lease`, and `lease_duration`. The function should calculate and return the remaining budget and total cost for each lease option. The `lease_duration` parameter is a list where the first element is the duration of the one-year lease and the second element is the duration of the two-year lease. The monthly expenses should be assumed to be the same for both lease options. The function should return a dictionary with the keys 'one_year_lease' and 'two_year_lease', each containing a dictionary with the keys 'remaining_budget' and 'total_cost'.
"""

def calculate_lease_options(monthly_expenses, one_year_lease, two_year_lease, lease_duration):
    """
    Calculate the remaining budget and total cost for each lease option.

    Args:
    monthly_expenses (int): The monthly expenses.
    one_year_lease (int): The monthly rent for the one-year lease.
    two_year_lease (int): The monthly rent for the two-year lease.
    lease_duration (list): A list containing the duration of the one-year lease and the two-year lease.

    Returns:
    dict: A dictionary with the keys 'one_year_lease' and 'two_year_lease', each containing a dictionary with the keys 'remaining_budget' and 'total_cost'.
    """

    # Calculate the remaining budget for each option
    remaining_budget_1 = monthly_expenses - one_year_lease
    remaining_budget_2 = monthly_expenses - two_year_lease

    # Calculate the total cost for each option
    total_cost_1 = one_year_lease * lease_duration[0]
    total_cost_2 = two_year_lease * lease_duration[1]

    # Return the results as a dictionary
    return {
        'one_year_lease': {
            'remaining_budget': remaining_budget_1,
            'total_cost': total_cost_1
        },
        'two_year_lease': {
            'remaining_budget': remaining_budget_2,
            'total_cost': total_cost_2
        }
    }