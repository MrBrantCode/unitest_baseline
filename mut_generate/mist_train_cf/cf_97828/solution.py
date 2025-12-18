"""
QUESTION:
Write a function `checkPrivilege` with parameters `isWhite`, `isPassing`, `hasPrivilege`, and `hasEconomicPrivilege` that returns a string describing the type of privilege a person has based on the input parameters. The function should account for all possible combinations of privileges, including white-passing privilege, economic privilege, class privilege, and no privilege. The returned string should be a clear and concise description of the person's privilege status.
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