"""
QUESTION:
Write a function `sort_logs(in_log: List[str]) -> List[str]` that takes in a list of log entries as strings, where each log entry consists of a unique identifier followed by a space and then the entry content. The function should return a list of log entries sorted according to the following criteria: letter-logs (logs with content containing only letters) should be sorted lexicographically by their content, in case of a tie, the identifier is used as a tie-breaker, and digit-logs (logs with content containing only digits) should appear in their original order.
"""

from typing import List

def sort_logs(in_log: List[str]) -> List[str]:
    letter_logs = []
    digit_logs = []
    
    for log in in_log:
        identifier, content = log.split(' ', 1)
        if content[0].isalpha():
            letter_logs.append((identifier, content))
        else:
            digit_logs.append(log)
    
    letter_logs.sort(key=lambda x: (x[1], x[0]))
    
    return [f"{identifier} {content}" for identifier, content in letter_logs] + digit_logs