"""
QUESTION:
Write a function `log_simulator(log_level)` that simulates a simple logging system. The function should accept a log level as input and then accept log messages from the user until the user enters "exit" to quit the program. The function should output log messages to the console based on the specified log level. Messages with a log level equal to or higher than the specified log level should be displayed. The log levels in order from highest to lowest are "emerg", "alert", "crit", "err", "warning", "notice", "info", "debug". The log level of each message is the first word before the colon in the message. If the log level is invalid, the function should print "Invalid log level" and stop.
"""

def log_simulator(log_level):
    """
    Simulates a simple logging system based on the specified log level.
    
    Args:
    log_level (str): The log level to filter messages by.
    
    Returns:
    None
    """

    log_levels = ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug"]
    
    if log_level not in log_levels:
        print("Invalid log level")
        return

    while True:
        message = input("Input log message: ")
        if message.lower() == "exit":
            break
        message_level = message.split(":")[0].strip().lower()
        if log_levels.index(message_level) <= log_levels.index(log_level):
            print(message)