"""
QUESTION:
Write a function `completed_goals_percentage` that takes in a list of boolean values representing the completion status of goals and returns the percentage of completed goals. The function should iterate through each goal in the list, count the number of completed goals (i.e., `True` values), and calculate the percentage of completed goals by dividing the number of completed goals by the total number of goals and multiplying by 100.
"""

def completed_goals_percentage(goals):
    completed_goals = 0   
    for goal in goals:    
        if goal:          
            completed_goals += 1    
    return (completed_goals / len(goals)) * 100    