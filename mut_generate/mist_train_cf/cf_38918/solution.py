"""
QUESTION:
Create a function `parse_ssh_command(ssh_cmd: str) -> dict` that takes a multi-line SSH command string as input, where each line may be split using the backslash character, and returns a dictionary containing the command and its arguments. The function should remove leading/trailing whitespace and quotes, and handle the case where the command and its arguments are split across multiple lines.
"""

import shlex

def parse_ssh_command(ssh_cmd: str) -> dict:
    # Remove leading/trailing whitespace and quotes
    ssh_cmd = ssh_cmd.strip().strip('"')
    
    # Replace backslash followed by newline with a space
    ssh_cmd = ssh_cmd.replace('\\\n', ' ')
    
    # Split the command into parts using shlex
    parts = shlex.split(ssh_cmd)
    
    # Extract the command and its arguments
    command = parts[0]
    arguments = parts[1:]
    
    return {
        "command": command,
        "arguments": arguments
    }