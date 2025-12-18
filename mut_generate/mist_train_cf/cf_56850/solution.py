"""
QUESTION:
Given a list of logs representing function calls with their start and end times and priorities, and the total number of functions `n`, implement a function named `exclusive_time(n, logs)` to return the exclusive time of each function in an array. The exclusive time of a function is the sum of its execution times for all function calls. 

The input `logs` is a list of strings, where each string represents a log message in the format "{function_id}:{'start' | 'end'}:{timestamp}:{priority}". The function should assume that all functions with the same priority are given in the logs in a correct order, i.e., the function with a smaller ID appears before the function with a larger ID if they both start at the same timestamp.

Constraints: `1 <= n <= 100`, `1 <= logs.length <= 500`, `0 <= function_id < n`, `0 <= timestamp <= 10^9`, and `1 <= priority <= 5`.
"""

def exclusive_time(n, logs):
    stack = []
    res = [0] * n
    prev_time = 0
    for log in logs:
        fn_id, typ, timestamp, _ = log.split(':')
        fn_id, timestamp = int(fn_id), int(timestamp)
        if typ == 'start':
            if stack:
                res[stack[-1]] += timestamp - prev_time
            stack.append(fn_id)
        else: # 'end'
            timestamp += 1 # adjust for inclusive end time
            res[stack.pop()] += timestamp - prev_time
        prev_time = timestamp
    return res