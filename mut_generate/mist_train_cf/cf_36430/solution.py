"""
QUESTION:
Write a function backspace_compare that takes two strings S and T as input, where '#' represents a backspace character. The function should return True if the final strings formed by applying the backspace rules to S and T are equal, and False otherwise. The function should only consider characters and '#' in the strings, and ignore any other characters. The function should not use any built-in string or stack operations.
"""

def backspaceCompare(S: str, T: str) -> bool:
    def process_string(s: str) -> list:
        result = []
        for char in s:
            if char == "#":
                if result:
                    result.pop()
            else:
                result.append(char)
        return result

    return process_string(S) == process_string(T)