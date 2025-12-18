"""
QUESTION:
Write a function `reorderLogFiles` that takes an array of logs as input. The function should reorder the logs according to the following rules:
- The letter-logs come before all digit-logs.
- The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers. If the contents and identifiers are the same, sort them based on the timestamp.
- The digit-logs maintain their relative ordering.

The input array `logs` consists of strings, where each string is a log. The length of `logs` is between 1 and 1000, and the length of each log is between 3 and 1000. Each log is guaranteed to have an identifier, at least one word after the identifier, and a timestamp.
"""

def reorderLogFiles(logs):
    def partition(log):
        id_, rest = log.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1,)
    
    return sorted(logs, key = partition)