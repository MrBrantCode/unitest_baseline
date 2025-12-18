"""
ORIGINAL QUESTION:
Write a function called `run_python_script` that takes the script's filename and operating system (Windows, macOS, or Linux) as input and returns a step-by-step guide on how to run the Python script using the command line interface, including any necessary precautions and differences based on the operating system. The function should return a string containing the instructions.
"""

def run_python_script(filename, operating_system):
    """
    This function provides a step-by-step guide on how to run a Python script using the command line interface.

    Args:
        filename (str): The name of the Python script file.
        operating_system (str): The operating system being used (Windows, macOS, or Linux).

    Returns:
        str: A string containing the instructions on how to run the Python script.
    """

    instructions = ""

    # Step 1: Open the terminal or command line interface
    instructions += "1. Open the terminal or command line interface.\n"
    if operating_system.lower() == "windows":
        instructions += "   - Press Windows + R keys, then type 'cmd' or 'powershell' and press Enter.\n"
    elif operating_system.lower() == "macos":
        instructions += "   - Use ⌘ + Spacebar, type 'terminal' and hit Enter.\n"
    elif operating_system.lower() == "linux":
        instructions += "   - Use Ctrl + Alt + T or go to the Applications menu and select 'Terminal'.\n"

    # Step 2: Navigate to the directory / folder where the Python script is located
    instructions += "\n2. Navigate to the directory / folder where the Python script is located using the 'cd' command.\n"
    instructions += "   Example: If your script is in a folder called 'scripts' in your home directory, you would type 'cd scripts' in your terminal and press enter.\n"

    # Step 3: Make sure that Python is installed and the path is set
    instructions += "\n3. Make sure that Python is installed and the path is set. You can check this by typing 'python --version' or 'python3 --version' in your terminal. If it outputs a Python version, that means Python is installed and path is set.\n"

    # Step 4: Run the Python script
    instructions += "\n4. Finally, run your Python script from the terminal by typing 'python " + filename + "' or 'python3 " + filename + "', depending on your Python version, and press Enter.\n"

    # Additional precautions and differences based on the operating system
    instructions += "\nAdditional Precautions and Differences:\n"
    if operating_system.lower() == "windows":
        instructions += "   - When setting up the development environment on Windows, you might need to add Python to your PATH manually. This can be done during Python installation or later by modifying Environment Variables in System Properties.\n"
    elif operating_system.lower() == "linux":
        instructions += "   - In Linux environments, the Python command is often linked to Python2 and python3 to Python3.\n"
    if operating_system.lower() in ["linux", "macos"]:
        instructions += "   - Linux and macOS operating systems are case sensitive so be sure to match the case in your script filename. Windows is not case sensitive.\n"

    # General precautions
    instructions += "\nGeneral Precautions:\n"
    instructions += "   - Ensure that the script doesn't contain malicious code, especially if it was obtained from an external source. Always review scripts before running them.\n"
    instructions += "   - It's also a good idea to have a shebang line at the top of your script ('#!/usr/bin/env python3') to ensure it runs with the correct version of Python.\n"

    return instructions