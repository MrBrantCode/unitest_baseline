"""
QUESTION:
Given a dictionary representing a person with properties "selfAwareness", "selfStability", and "selfConfidence", create a function `evaluatePerson` that returns a string describing the person's mental state based on the following conditions:

- If "selfAwareness" is true and "selfStability" is false, return "This person may struggle with self-doubt and indecision."
- If "selfAwareness" and "selfStability" are both true, and "selfConfidence" is true, return "This person exhibits a healthy level of self-confidence and self-awareness."
- If "selfAwareness" and "selfStability" are both true, and "selfConfidence" is false, return "This person has a great balance of self-confidence, self-awareness, and self-stability."
- Otherwise, return "This person lacks self-awareness and stability."
"""

def evaluatePerson(person):
    if person["selfAwareness"] and not person["selfStability"]:
        return "This person may struggle with self-doubt and indecision."
    elif person["selfAwareness"] and person["selfStability"]:
        if person["selfConfidence"]: 
            return "This person exhibits a healthy level of self-confidence and self-awareness."
        else:
            return "This person has a great balance of self-confidence, self-awareness, and self-stability."
    else:
        return "This person lacks self-awareness and stability."