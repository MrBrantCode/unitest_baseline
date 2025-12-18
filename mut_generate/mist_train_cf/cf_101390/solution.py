"""
QUESTION:
Implement a function named `calculate_total_bill` that takes two parameters: `num_customers` (an integer) and `order_total` (a float). The function must calculate the total bill for a group of customers, considering a minimum order requirement of $50 and applying discounts based on the number of customers: 5% for 1-5 people, 10% for 6-10 people, and 15% plus an additional 5% for more than 10 people. If the order total is less than $50, return an error message. The function should return the total bill rounded to 2 decimal places.
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