"""
QUESTION:
Create a Python function `admin_task_help` that takes two parameters: `command_type` and `pattern`. The `command_type` parameter is a required string representing the type of command for which help information is requested. It can be either "-commands", "-commandGroups", or a specific command name. The `pattern` parameter is an optional string representing the pattern to match when retrieving commands or command groups, defaulting to an empty string if not provided.

The function should return the help information based on the provided `command_type` and `pattern`. If `command_type` is "-commands", return a list of commands matching the specified pattern. If `command_type` is "-commandGroups", return a list of command groups. If `command_type` is a specific command name, return detailed help information for that command.
"""

def admin_task_help(command_type, pattern=""):
    # Simulating the behavior of AdminTask.help function in WebSphere Application Server
    if command_type == "-commands":
        # Simulate retrieving a list of commands matching the specified pattern
        if pattern == "*jvm*":
            return ["startJvm", "stopJvm", "listJvm"]
        elif pattern == "*user*":
            return ["createUser", "deleteUser", "updateUser"]
        else:
            return []  # Return empty list if no matching commands found
    elif command_type == "-commandGroups":
        # Simulate retrieving a list of command groups
        return ["ServerManagement", "UserManagement", "JVMManagement"]
    else:
        # Simulate retrieving detailed help information for a specific command
        if command_type == "listNodes":
            return "Command: listNodes\nDescription: Lists all the nodes in the cell."
        elif command_type == "listServers":
            return "Command: listServers\nDescription: Lists all the servers in the cell."
        elif command_type == "showServerInfo":
            return "Command: showServerInfo\nDescription: Displays detailed information about a specific server."
        else:
            return "Command not found"  # Return message for unknown command