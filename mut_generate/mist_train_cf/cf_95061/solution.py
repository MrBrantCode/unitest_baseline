"""
QUESTION:
Create a function called `sum_command_line_args` that takes a list of command line arguments as input. The function should return the sum of the numeric arguments. If any non-numeric arguments are found, the function should print an error message listing all the non-numeric arguments. Assume that the input list does not contain the script name, only the actual command line arguments.
"""

def sum_command_line_args(args):
    sum_result = 0
    error_args = []

    for arg in args:
        try:
            sum_result += float(arg)
        except ValueError:
            error_args.append(arg)

    if error_args:
        error_message = "The following arguments are not numeric: " + ", ".join(error_args)
        print(error_message)

    return sum_result