"""
QUESTION:
Implement the `Logger` class with a constructor that takes a `name` parameter and initializes an empty list to store log messages. The class should have two methods: `log(message, level)` and `get_logs(name, level)`. The `log` method takes a `message` and a `level` (an integer from 1 to 3) and appends a tuple `(message, level)` to the list of log messages. The `get_logs` method takes a `name` and a `level` and returns a list of log messages with the given `name` and severity level greater than or equal to the specified `level`. If `name` is `None`, it should return log messages from all loggers.

Additionally, implement a function `getLogger(name)` that returns a `Logger` instance with the given name if it already exists, or creates a new `Logger` instance with the given name.
"""

class Logger:
    def __init__(self, name):
        self.name = name
        self.logs = []

    def log(self, message, level):
        self.logs.append((message, level))

    def get_logs(self, name, level):
        if name is None:
            return [(msg, lvl) for msg, lvl in self.logs if lvl >= level]
        else:
            return [(msg, lvl) for msg, lvl in self.logs if self.name == name and lvl >= level]

def getLogger(name):
    if name in getLogger.loggers:
        return getLogger.loggers[name]
    else:
        logger = Logger(name)
        getLogger.loggers[name] = logger
        return logger

getLogger.loggers = {}