"""
QUESTION:
Write a function `parseFlags(args, flags)` that takes a list of command-line arguments `args` and a list of flags `flags` as input. The function should parse the command-line arguments and extract the values for the specified flags, returning a dictionary containing the values for the specified flags. If a flag is not present in the arguments, its value should be set to `None`.
"""

def parseFlags(args, flags):
    flag_values = {}
    i = 0
    while i < len(args):
        if args[i] in ['-{}'.format(flag) for flag in flags]:
            flag = args[i].lstrip('-')
            value = args[i + 1] if i + 1 < len(args) else None
            flag_values[flag] = value
            i += 1
        i += 1
    for flag in flags:
        if flag not in flag_values:
            flag_values[flag] = None
    return flag_values