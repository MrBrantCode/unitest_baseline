"""
QUESTION:
Write a function `analyze_log` that takes a string `log_content` as input and returns a list of dictionaries. Each dictionary should contain information for a host, including the hostname and the number of PASS, FAIL, WARN, INFO entries, and fatal errors. The function should parse the log content, which consists of log entries in the format "hostname: [status_type] message", and extract the required information. If a fatal error is encountered, the function should handle it accordingly. The function should return the list of dictionaries, sorted by hostname. 

The input `log_content` is a string containing the log file content, and the function returns a list of dictionaries, each containing the information for a host. The dictionary keys should be 'hostname', 'PASS', 'FAIL', 'WARN', 'INFO', and 'fatal_errors', and the values should be strings and integers.
"""

from typing import List, Dict, Union

def analyze_log(log_content: str) -> List[Dict[str, Union[str, int]]]:
    host_data = {}
    for line in log_content.split('\n'):
        if line:
            host, status = line.split(': [', 1)
            status_type, _ = status.split(']', 1)
            if host not in host_data:
                host_data[host] = {'hostname': host, 'PASS': 0, 'FAIL': 0, 'WARN': 0, 'INFO': 0, 'fatal_errors': 0}
            if status_type == 'PASS':
                host_data[host]['PASS'] += 1
            elif status_type == 'FAIL':
                host_data[host]['FAIL'] += 1
            elif status_type == 'WARN':
                host_data[host]['WARN'] += 1
            elif status_type == 'INFO':
                host_data[host]['INFO'] += 1
            elif status_type == 'FATAL ERROR':
                host_data[host]['fatal_errors'] += 1

    result = [data for _, data in host_data.items()]
    return sorted(result, key=lambda x: x['hostname'])