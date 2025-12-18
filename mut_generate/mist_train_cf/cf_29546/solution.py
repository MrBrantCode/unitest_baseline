"""
QUESTION:
Implement the `ArgumentManager` class with the following methods: `add_argument(arg)`, `remove_argument(arg)`, `update_argument(old_arg, new_arg)`, and `parse_arguments()`. The class should have an attribute `args` to store the list of command-line arguments. 

When `add_argument(arg)` is called, the argument should be added to `args` only if it does not already exist. When `remove_argument(arg)` is called, the specified argument should be removed from `args` if it exists; otherwise, an error message should be printed. When `update_argument(old_arg, new_arg)` is called, the specified argument should be updated with a new value if it exists; otherwise, an error message should be printed. The `parse_arguments()` method should parse the command-line arguments, removing any duplicates and updating the `args` attribute with the parsed arguments.
"""

def ArgumentManager(args):
    new_args = []
    for arg in args:
        if arg not in new_args:
            new_args.append(arg)
        else:
            print('Error: Duplicate argument detected.')
    return new_args