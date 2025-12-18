"""
QUESTION:
Implement a function `change_directory` that simulates the behavior of the "cd" command in a Unix-like operating system. The function takes two parameters: `current_path` and `command`, both strings representing directory paths separated by forward slashes. The `command` can be a relative or absolute path. If `command` is a relative path, apply it to `current_path`; if `command` is an absolute path, replace `current_path` entirely. Return the new directory path after executing the command.
"""

def change_directory(current_path: str, command: str) -> str:
    if command.startswith("/"):  # Absolute path
        return command
    else:  # Relative path
        directories = current_path.split("/")
        commands = command.split("/")
        for cmd in commands:
            if cmd == "..":
                directories = directories[:-1]
            elif cmd != "" and cmd != ".":
                directories.append(cmd)
        return "/".join(directories)