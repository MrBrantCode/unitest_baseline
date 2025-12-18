"""
QUESTION:
Divide a fortune between two children and charity. The function should be named `allocate_fortune`. The function takes an integer `total_fortune` and returns a list of three values: the amount allocated to the first child, the second child, and the charity, respectively. The amount allocated to the second child should be 25% more than the first child, and the amount allocated to the charity should be 5% of the total fortune.
"""

def allocate_fortune(total_fortune):
    charity_allocation = total_fortune * 0.05
    remaining_fortune = total_fortune - charity_allocation
    first_child_allocation = remaining_fortune / 2.25
    second_child_allocation = first_child_allocation * 1.25
    return [round(first_child_allocation, 3), round(second_child_allocation, 3), round(charity_allocation, 3)]