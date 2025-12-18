"""
QUESTION:
Create a function `simulate_file_system` that simulates a simple file system operation. The function takes a list of commands as input, executes them, and returns a list of strings representing the output of the `ls` command at the end of the simulation. The commands can be `mkdir <directory_name>`, `touch <file_name>`, `rm <file_or_directory_name>`, or `ls`. The function should handle these commands accordingly: create a new directory, create a new file, remove a file or directory, or list the contents of the current directory, respectively.
"""

def simulate_file_system(commands):
    file_system = {}

    def mkdir(directory_name):
        file_system[directory_name] = []

    def touch(file_name):
        current_directory = file_system.get('current', [])
        current_directory.append(file_name)
        file_system['current'] = current_directory

    def rm(file_or_directory_name):
        if file_or_directory_name in file_system:
            del file_system[file_or_directory_name]
        else:
            current_directory = file_system.get('current', [])
            if file_or_directory_name in current_directory:
                current_directory.remove(file_or_directory_name)
                file_system['current'] = current_directory

    def ls():
        current_directory = file_system.get('current', [])
        return sorted(list(file_system.keys()) + current_directory)

    for command in commands:
        parts = command.split()
        if parts[0] == 'mkdir':
            mkdir(parts[1])
        elif parts[0] == 'touch':
            touch(parts[1])
        elif parts[0] == 'rm':
            rm(parts[1])
        elif parts[0] == 'ls':
            ls()

    return ls()