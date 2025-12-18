"""
QUESTION:
Implement a function `generate_send_to_spark_command` that generates a string representing a command to send a variable to a Spark cluster. The function should take two parameters: `variable` (a Pandas DataFrame or a string) and `var_name` (a string representing the name of the variable). The returned string should be in the format `%%send_to_spark -i var_name -t type_of_variable -n var_name`, where `type_of_variable` is "str" if the variable is a string and "pandas" otherwise.
"""

def generate_send_to_spark_command(variable, var_name):
    if isinstance(variable, str):
        type_of_variable = "str"
    else:
        type_of_variable = "pandas"
    
    return f"%%send_to_spark -i {var_name} -t {type_of_variable} -n {var_name}"