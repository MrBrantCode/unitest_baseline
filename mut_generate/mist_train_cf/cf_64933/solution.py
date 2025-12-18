"""
QUESTION:
Given a series of cash flows C[0], C[1], C[2], ..., C[N] and a discount rate 'r', write a function named 'present_value' to calculate the total present value of the cash flows. The function should take two parameters: a list of cash flows and the discount rate. The cash flows happen at the end of each period, and C[0] is the current cash flow.
"""

def present_value(cash_flows, discount_rate):
    """
    Calculate the total present value of a series of cash flows.

    Args:
        cash_flows (list): A list of cash flows, where cash_flows[0] is the current cash flow.
        discount_rate (float): The discount rate.

    Returns:
        float: The total present value of the cash flows.
    """
    return sum(cf / (1 + discount_rate)**i for i, cf in enumerate(cash_flows))