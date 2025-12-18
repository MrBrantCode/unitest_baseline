"""
QUESTION:
Write a function `calc_spendings(salary, spendings)` that accepts a monthly salary and a dictionary of spending categories with their corresponding percentages. The function should calculate and print the amount spent on each category and the savings, handling error cases where inputs may not be numerical or the percentages sum to over 100%. The function should take a string representation of the salary and a dictionary where the keys are the spending categories and the values are string representations of the percentages of salary spent on those categories.
"""

def entrance(salary, spendings):
    """
    Calculate and print the amount spent on each category and the savings.

    Args:
        salary (str): A string representation of the monthly salary.
        spendings (dict): A dictionary where the keys are the spending categories and 
            the values are string representations of the percentages of salary spent on those categories.

    Returns:
        None
    """

    # convert from string to float
    try:
        salary = float(salary)
    except ValueError:
        print("Salary must be a numerical value.")
        return

    # check if total spending is more than 100%
    total_percentage = 0.0
    for category, percentage in spendings.items():
        # convert percentage to float
        try:
            spendings[category] = float(percentage)
        except ValueError:
            print("Spending percentages must be numerical values.")
            return
        total_percentage += spendings[category]

    if total_percentage > 100.0:
        print("Total spending percentages cannot exceed 100%.")
        return


    total_spendings = 0.0
    for category, percentage in spendings.items():
        spent = (percentage / 100.0) * salary
        total_spendings += spent
        print(f"{category}: {spent}")

    savings = salary - total_spendings
    print(f"Savings: {savings}")