"""
QUESTION:
Implement the `simulate_file_system` function, which simulates a simple file system navigation system. The function takes a list of commands as input and returns the final current directory path after executing the commands. The initial directory is always "/".

The commands can be one of the following: 
- "mkdir <directory_name>" to create a new directory with the given name.
- "cd <directory_name>" to change the current directory to the specified directory.
- "pwd" to print the current directory path.

Note that the function does not need to print anything, but rather return the final current directory path. Also, the function should not handle any invalid commands.
"""

def simulate_file_system(commands):
    current_path = "/"
    directory_structure = {"/": []}

    for command in commands:
        if command.startswith("mkdir"):
            directory_name = command.split()[1]
            directory_structure[current_path].append(directory_name)
            directory_structure["/" + directory_name] = []
        elif command.startswith("cd"):
            directory_name = command.split()[1]
            if directory_name == "..":
                current_path = "/".join(current_path.split("/")[:-2]) + "/"
            else:
                current_path += directory_name + "/"
        elif command == "pwd":
            return current_path

    return current_path