"""
QUESTION:
Create a function `process_conditions` that takes an array of conditions as input. The function should iterate over each condition in the array. If the condition is a boolean, it should append a message to the output list indicating whether the condition is True or False. If the condition is not a boolean, it should append an error message to the output list. The function should return the list of messages.
"""

def process_conditions(conditions):
    output = []
    for condition in conditions:
        if type(condition) != bool:
            output.append("Error: Non-boolean value detected")
            continue

        if condition:
            message = "Condition is True"
        else:
            message = "Condition is False"
        output.append(message)
    
    return output