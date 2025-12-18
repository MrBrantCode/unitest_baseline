"""
QUESTION:
Write a function named `calculate_total_bill` that takes two parameters, `num_people` and `total_bill`, where `num_people` is the number of people in the group and `total_bill` is the total amount to be paid before the discount is applied. The function should apply a discount to the total bill based on the number of people: 5% for 2-3 people, 10% for 4-6 people, 15% for 7-10 people, and 20% for 11 or more people, then return the total bill after subtracting the discount.
"""

def calculate_total_bill(num_people, total_bill):
    if num_people <= 3:
        discount = total_bill * 0.05
    elif num_people <= 6:
        discount = total_bill * 0.1
    elif num_people <= 10:
        discount = total_bill * 0.15
    else:
        discount = total_bill * 0.2
        
    return total_bill - discount