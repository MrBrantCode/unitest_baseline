"""
QUESTION:
Create a function `calculate_activity_portfolio` that takes a dictionary `args` with activity names as keys and their corresponding weights as values, and an optional dictionary `report_data` with additional data for each activity. The function should calculate the total weight of all activities, incorporate the additional data into the portfolio report if `report_data` is provided, and return a portfolio report dictionary with the total weight and activity weights, as well as the additional data if available. The weights should be represented as floating-point numbers.
"""

def calculate_activity_portfolio(args, report_data=None):
    total_weight = sum(args.values())
    portfolio_report = {
        "total_weight": total_weight,
        "activities": args
    }
    if report_data:
        portfolio_report["report_data"] = report_data
    return portfolio_report