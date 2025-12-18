"""
QUESTION:
Create a function `calculate_discount` that takes the number of children as input and returns the total discount percentage for the group. The discount rates are as follows: 
- 2 children: 10% discount
- 3 children: 15% discount
- 4 children: 18% discount
- 5 or more children: 18% discount for the first 4 children, and an additional 1% discount for each additional child beyond 4.
"""

def calculate_discount(num_children: int) -> int:
    if num_children == 2:
        discount_total = 10
    elif num_children == 3:
        discount_total = 15
    elif num_children == 4:
        discount_total = 18
    elif num_children >= 5:
        discount_total = 18 + (num_children - 4)
    return discount_total