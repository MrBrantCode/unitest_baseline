"""
QUESTION:
Implement a function `calculate_total_bill` that takes two parameters: `num_customers` (an integer representing the number of customers in a group) and `order_total` (a float representing the total cost of the order). The function should apply discounts based on the number of customers: 5% for 5 or fewer people, 10% for 6-10 people, and 15% for more than 10 people. However, a minimum order of $50 is required to avail of discounts. If the order total is less than $50, return the message "Order total does not meet the minimum amount required to avail of discounts." Otherwise, return the total bill rounded to 2 decimal places.
"""

def calculate_total_bill(num_customers, order_total):
    # Check if the order meets the minimum amount required to avail of discounts
    if order_total < 50:
        return "Order total does not meet the minimum amount required to avail of discounts."

    # Calculate the total bill without discounts
    total_bill = order_total

    # Apply discounts based on the number of customers in the group
    if num_customers <= 5:
        total_bill *= 0.95
    elif num_customers <= 10:
        total_bill *= 0.9
    else:
        total_bill *= 0.85

    # Return the total bill rounded to 2 decimal places
    return round(total_bill, 2)