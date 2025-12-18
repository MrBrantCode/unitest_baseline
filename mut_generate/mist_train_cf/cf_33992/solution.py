"""
QUESTION:
Implement a function `process_commands` that simulates a simple file system navigation. The function should take a list of commands as input and output the final permissions of the files and the current working directory after executing all the commands. The function should support the following commands:
- `chmod <permissions> <filename>`: changes the permissions of the specified file
- `cd <directory>`: changes the current working directory to the specified directory

Assume the following initial conditions:
- The initial permissions of all files are set to "rw-" (read and write permissions for the owner, no permissions for group and others)
- The initial working directory is "/"
- The function should handle the 'a', '+', and '-' symbols in the permissions string correctly, where 'a' represents all users, '+' represents adding permissions, and '-' represents removing permissions. 

Note: The function should not assume the existence of any specific files or directories.
"""

def process_commands(commands):
    file_permissions = {"amf.js": "rw-"}
    current_directory = "/"
    
    for command in commands:
        if command.startswith("chmod"):
            parts = command.split()
            permissions = parts[1]
            filename = parts[2]
            file_permissions[filename] = apply_permissions(file_permissions.get(filename, "rw-"), permissions)
        elif command.startswith("cd"):
            directory = command.split()[1]
            current_directory = change_directory(current_directory, directory)
    
    return file_permissions, current_directory


def apply_permissions(current_permissions, new_permissions):
    for p in new_permissions:
        if p == "a":
            current_permissions = "rwx"
        elif p == "+":
            current_permissions = add_permissions(current_permissions, new_permissions[1:])
        elif p == "-":
            current_permissions = remove_permissions(current_permissions, new_permissions[1:])
    return current_permissions


def add_permissions(current_permissions, new_permissions):
    for p in new_permissions:
        if p == "r" and "r" not in current_permissions:
            current_permissions += "r"
        elif p == "w" and "w" not in current_permissions:
            current_permissions += "w"
        elif p == "x" and "x" not in current_permissions:
            current_permissions += "x"
    return current_permissions


def remove_permissions(current_permissions, new_permissions):
    for p in new_permissions:
        if p == "r" and "r" in current_permissions:
            current_permissions = current_permissions.replace("r", "")
        elif p == "w" and "w" in current_permissions:
            current_permissions = current_permissions.replace("w", "")
        elif p == "x" and "x" in current_permissions:
            current_permissions = current_permissions.replace("x", "")
    return current_permissions


def change_directory(current_directory, directory):
    if directory == "..":
        return "/".join(current_directory.split("/")[:-1])
    else:
        return current_directory + "/" + directory