"""
QUESTION:
Implement the runAsAdmin function that takes a list of actions (install, debug, code) and returns a list of methods to ensure developers can perform these actions without running as administrators. The function should consider the following methods: User Access Control (UAC), Windows Principle of Least Privilege (POLP), Run As Different User, Use of Virtual Machines, Network Security, and Local Administrator Password Solution (LAPS).
"""

def runAsAdmin(actions):
    """
    This function takes a list of actions (install, debug, code) and returns a list of methods 
    to ensure developers can perform these actions without running as administrators.

    Args:
        actions (list): A list of actions (install, debug, code)

    Returns:
        list: A list of methods to ensure developers can perform actions without running as administrators
    """

    methods = {
        'install': ['UAC', 'Run As Different User', 'Use of Virtual Machines', 'LAPS'],
        'debug': ['UAC', 'Run As Different User', 'Use of Virtual Machines'],
        'code': ['Windows Principle of Least Privilege (POLP)', 'Network Security']
    }

    result = []
    for action in actions:
        if action in methods:
            result.extend(methods[action])

    # Remove duplicates
    result = list(set(result))

    return result