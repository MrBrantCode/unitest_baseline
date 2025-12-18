"""
QUESTION:
Write a function `analyzeStatus` that takes a string of nested status messages as input, where each message starts with "The status should be" followed by a status value ("success" or "failure") and ends with "End". The function should return the overall status as "success" if all nested messages contain "success" and "failure" otherwise. The input string is formatted with indentation representing nested messages.
"""

def analyzeStatus(status: str) -> str:
    stack = []
    for line in status.split('\n'):
        if line.startswith("The status should be"):
            stack.append(line.split()[-1])
        elif line == "End":
            if "failure" in stack:
                return "failure"
            stack.pop()
    return "success"