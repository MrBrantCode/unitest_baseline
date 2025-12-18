"""
QUESTION:
Implement the `process_data` function that takes a list of dictionaries `mem_data` as input, where each dictionary contains a 'timestamp' (unix timestamp) and a nested 'mem' dictionary with a 'percent' key representing memory usage percentage. The function should return a dictionary with two lists: "data_time" containing formatted date-time strings (MMDD-HH:MM) corresponding to the timestamps, and "mem_percent" containing the extracted memory percentages.
"""

import time

def process_data(mem_data):
    data_time = []
    mem_percent = []

    for doc in mem_data:
        unix_time = doc['timestamp']
        times = time.localtime(unix_time)
        dt = time.strftime("%m%d-%H:%M", times)
        data_time.append(dt)
        m_percent = doc['mem']['percent']
        mem_percent.append(m_percent)

    data = {"data_time": data_time, "mem_percent": mem_percent}
    return data