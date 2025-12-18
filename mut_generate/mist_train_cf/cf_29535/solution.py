"""
QUESTION:
Reorder the given list of log entries such that all the letter-logs come before the digit-logs. The letter-logs should be ordered lexicographically ignoring the identifier, with the identifier used in case of ties. The digit-logs should remain in the same order they were in the input.

Write a function `reorderLogFiles(logs: List[str])` to reorder the logs. The function takes a list of strings representing the log entries as input, where each log entry consists of a unique identifier followed by some words, with the identifier consisting of only digits, and the words in the log separated by spaces. The function should return a list of strings representing the reordered log entries.
"""

from typing import List

def reorderLogFiles(logs: List[str]) -> List[str]:
    letter_logs = []
    digit_logs = []
    
    for log in logs:
        if log.split()[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)
    
    letter_logs.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))
    
    return letter_logs + digit_logs