"""
QUESTION:
Create a function called `process_command` that takes a string representing a command and its arguments. The function should support two commands: "jekyll build" and "jekyll build --drafts". For the "jekyll build" command, return "Site built successfully". For the "jekyll build --drafts" command, return "Site built successfully, including drafts". For any other command, return "Error: Command not recognized".
"""

def process_command(command):
    if command == "jekyll build":
        return "Site built successfully"
    elif command == "jekyll build --drafts":
        return "Site built successfully, including drafts"
    else:
        return "Error: Command not recognized"