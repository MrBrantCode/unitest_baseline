"""
QUESTION:
Create a function named `checkPrivilege` that takes four parameters: `isWhite`, `isPassing`, `hasPrivilege`, and `hasEconomicPrivilege`. The function should return a string describing the individual's privilege level based on the input parameters. Each parameter should be a boolean value indicating whether the individual has the corresponding privilege. The function should account for all possible combinations of privilege, including scenarios where an individual has one or more types of privilege but not others.
"""

def checkPrivilege(isWhite, isPassing, hasPrivilege, hasEconomicPrivilege):
    if isWhite and isPassing and hasPrivilege and hasEconomicPrivilege:
        return "You are privileged in every sense of the word."
    elif isWhite and isPassing and hasPrivilege:
        return "You have white-passing privilege and class privilege."
    elif isWhite and hasPrivilege and hasEconomicPrivilege:
        return "You have white privilege and class privilege."
    elif isWhite and isPassing:
        return "You have white-passing privilege."
    elif isWhite and hasPrivilege:
        return "You have white privilege and class privilege."
    elif isPassing and hasPrivilege and hasEconomicPrivilege:
        return "You have class privilege."
    elif hasPrivilege and hasEconomicPrivilege:
        return "You have class privilege."
    elif isWhite:
        return "You have white privilege."
    elif hasPrivilege:
        return "You have class privilege."
    else:
        return "You don't have any privilege."