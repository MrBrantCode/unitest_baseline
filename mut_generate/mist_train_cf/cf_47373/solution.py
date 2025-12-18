"""
QUESTION:
Create a function named `check_variables` that takes two variables as input and returns a dictionary. The function should first check if the two input variables have the same type and include the result in the dictionary with the key "same_type". Then, for each variable, the function should check the following conditions based on its data type:
- If the variable is a string, check if its length is equal to or greater than 5.
- If the variable is an integer or a float, check if it is a positive number.
- If the variable is a list, check if the length of the list is even.
The function should include the results of these checks in the dictionary with dynamic keys in the format "var{}_str_len_ge_5", "var{}_is_positive", and "var{}_list_len_is_even", where {} is the variable index (1 or 2).
"""

def check_variables(var1, var2):
    result = {
        "same_type": type(var1) == type(var2)
    }
    
    for i, var in enumerate([var1, var2], start=1):
        if isinstance(var, str):
            key = "var{}_str_len_ge_5".format(i)
            result[key] = len(var) >= 5
        elif isinstance(var, (int, float)):
            key = "var{}_is_positive".format(i)
            result[key] = var > 0
        elif isinstance(var, list):
            key = "var{}_list_len_is_even".format(i)
            result[key] = len(var) % 2 == 0
            
    return result