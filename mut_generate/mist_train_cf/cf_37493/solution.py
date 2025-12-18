"""
QUESTION:
Implement the `parse_command_parameter` function to take a string of commands separated by "+" and return a list of valid commands. The valid commands are limited to "show", "package", "verify", "upload", "download", and "install". If any command in the input string is not one of these, the function should raise an error.
"""

import argparse

available_commands = ["show", "package", "verify", "upload", "download", "install"]

def parse_command_parameter(argument_value):
    command_list = argument_value.split("+")
    for command in command_list:
        if command not in available_commands:
            raise argparse.ArgumentTypeError("invalid artifact command: '%s'" % command)
    return command_list