"""
QUESTION:
Write a function named `navigate_directory` that simulates a simplified version of a file system navigation tool. The function takes a string of commands as input, where each command is separated by ' && ', and outputs the final directory location after executing the commands. 

The commands can be either `cd <directory>` to change the current directory to the specified directory, or `..` to move up one level in the directory hierarchy. The directory structure is represented as a Unix-like file system and the initial directory is '/'.
"""

def navigate_directory(commands):
    current_directory = '/'
    command_list = commands.split(' && ')
    
    def change_directory(current, new):
        if new.startswith('/'):
            return new
        else:
            return current + new + '/'

    def move_up_directory(current):
        if current == '/':
            return '/'
        else:
            return '/'.join(current.split('/')[:-2]) + '/'

    for command in command_list:
        if command.startswith('cd'):
            directory = command.split(' ')[1]
            current_directory = change_directory(current_directory, directory)
        elif command == '..':
            current_directory = move_up_directory(current_directory)
    
    return current_directory