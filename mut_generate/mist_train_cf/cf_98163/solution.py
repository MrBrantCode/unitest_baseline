"""
QUESTION:
Create a method called "promote" for the "Employee" class. The method should automatically promote an employee to a higher rank based on their performance. If the performance is above 90, promote to "Manager". If the performance is above 80, promote to "Senior Employee". If the performance is above 70, promote to "Intermediate Employee". Otherwise, keep the rank as "Junior Employee".
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