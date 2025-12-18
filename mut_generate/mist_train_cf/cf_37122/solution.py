"""
QUESTION:
Implement the function `parse_arguments(args_spec)` that takes a list of argument specifications and returns a dictionary containing the parsed arguments. 

Each argument specification is a tuple in the format `(argument_name, argument_type, help_message, default_value)`, where `argument_name` is the name of the argument, `argument_type` is a string representing the data type of the argument (e.g., "int", "str", "float"), `help_message` is a brief description of the argument, and `default_value` is the default value for the argument (optional). 

The function should support both positional and optional arguments, where optional arguments are specified with a "--" prefix, and return a dictionary containing the parsed values with the argument names as keys.
"""

import argparse

def parse_arguments(args_spec):
    parser = argparse.ArgumentParser(description="Argument Parser")
    
    for arg_spec in args_spec:
        if arg_spec[0].startswith("--"):
            arg_name = arg_spec[0][2:]
            arg_type = arg_spec[1]
            help_msg = arg_spec[2]
            default_val = arg_spec[3] if len(arg_spec) == 4 else None
            parser.add_argument(f"--{arg_name}", type=eval(arg_type), help=help_msg, default=default_val)
        else:
            arg_name = arg_spec[0]
            arg_type = arg_spec[1]
            help_msg = arg_spec[2]
            parser.add_argument(arg_name, type=eval(arg_type), help=help_msg)
    
    args = vars(parser.parse_args())
    return args