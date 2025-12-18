"""
QUESTION:
Create a method `promote` in the `Employee` class to automatically promote an employee to a higher rank based on their performance. The method should check the employee's performance and update their rank accordingly. The rank thresholds are as follows: Manager (above 90%), Senior Employee (above 80%), Intermediate Employee (above 70%), and Junior Employee (below 70%).
"""

def promote(performance):
    if performance > 90:
        return "Manager"
    elif performance > 80:
        return "Senior Employee"
    elif performance > 70:
        return "Intermediate Employee"
    else:
        return "Junior Employee"