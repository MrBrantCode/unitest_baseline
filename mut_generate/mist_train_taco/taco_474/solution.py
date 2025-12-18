"""
QUESTION:
Thanks to the effects of El Nino this year my holiday snorkelling trip was akin to being in a washing machine... Not fun at all.

Given a string made up of '~' and '\_' representing waves and calm respectively, your job is to check whether a person would become seasick.

Remember, only the process of change from wave to calm (and vice versa) will add to the effect (really wave peak to trough but this will do). Find out how many changes in level the string has and if that figure is more than 20% of the string, return "Throw Up", if less, return "No Problem".
"""

def check_seasickness(sea: str) -> str:
    # Calculate the number of level changes
    level_changes = sea.count('~_') + sea.count('_~')
    
    # Calculate the percentage of level changes
    change_percentage = level_changes / len(sea)
    
    # Determine if the person would become seasick
    if change_percentage > 0.2:
        return "Throw Up"
    else:
        return "No Problem"