"""
QUESTION:
Implement a function `file_system_navigation(commands)` that simulates a simple file system navigation tool. The function takes a list of commands as input, where each command can be one of the following: `cd <directory>` to change the current directory, `./<file>` to execute a file in the current directory, or `pwd` to print the current working directory. The function should return a list of output messages based on the given commands, assuming the initial working directory is `/`.
"""

def entance(commands):
    current_directory = '/'
    output = []

    for command in commands:
        if command.startswith('cd'):
            directory = command.split(' ')[1]
            if directory.startswith('/'):
                current_directory = directory
            else:
                current_directory = current_directory + '/' + directory if current_directory != '/' else '/' + directory
        elif command.startswith('./'):
            file = command[2:]
            output.append(f'Executing {file}...')
        elif command == 'pwd':
            output.append(current_directory)

    return output