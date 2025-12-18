"""
QUESTION:
Implement a function `generateWarningMessage(username, condition)` that generates personalized warning messages for individuals entering the #dogpark based on their usernames and specific conditions. The function should take in the `username` of the individual and a `condition` indicating the specific scenario, and return a personalized warning message based on the given condition and the username. The function should support conditions 1, 2, and 3, corresponding to the following warning message templates: 
1. "@%s beware - flesh entering the #dogpark without correct papers will actually turn into a liquid."
2. "Only truely evil spirits may enter the #dogpark. Are you one of us, @%s?"
3. "I heard a five headed dragon near the #dogpark might try to dine on @%s."
Replace the `%s` in the templates with the provided `username`. Return "Invalid condition provided." for any other condition.
"""

def entrance(username, condition):
    if condition == 1:
        return "@%s beware - flesh entering the #dogpark without correct papers will actually turn into a liquid." % username
    elif condition == 2:
        return "Only truely evil spirits may enter the #dogpark. Are you one of us, @%s?" % username
    elif condition == 3:
        return "I heard a five headed dragon near the #dogpark might try to dine on @%s." % username
    else:
        return "Invalid condition provided."