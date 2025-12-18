"""
QUESTION:
Implement the function `process_commands(commands)` that takes a list of commands as input, where each command is a string in the format "variable = value if condition". The condition is in the format "variable comparison value", where comparison can be one of "=", "<", ">". Update a dictionary according to the rules specified in the commands, where the dictionary is initially empty. If a condition is met, assign the variable a value of 0 in the dictionary, otherwise skip the assignment. Return the updated dictionary.
"""

def process_commands(commands):
    dictionary = {}

    for command in commands:
        assignment, condition = command.split(" if ")
        var, value = assignment.split(" = ")
        condition_var, comparison, condition_value = condition.split()

        if condition_var in dictionary:
            condition_var_value = dictionary[condition_var]
        else:
            condition_var_value = 0

        if comparison == ">":
            if condition_var_value > int(condition_value):
                dictionary[var] = 0
        elif comparison == "<":
            if condition_var_value < int(condition_value):
                dictionary[var] = 0
        elif comparison == "=":
            if condition_var_value == int(condition_value):
                dictionary[var] = 0

    return dictionary