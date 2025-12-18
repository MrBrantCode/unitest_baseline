"""
QUESTION:
Implement a function `parse_http_log(log: dict) -> dict` that takes a dictionary representing an HTTP request and response log as input and returns a new dictionary containing specific extracted information. The input log dictionary has keys such as "connect", "send", "reply", and "header" with corresponding data values. The output dictionary should include the host and port from the "connect" action, the HTTP method and path from the "send" action, the HTTP status code from the "reply" action, and the server information from the "header" action.
"""

def parse_http_log(log: dict) -> dict:
    parsed_log = {}

    # Extract connection information
    if 'connect' in log:
        host, port = log['connect'].split(":")
        parsed_log['host'] = host
        parsed_log['port'] = port

    # Extract request method and path
    if 'send' in log:
        send_data = log['send'].decode('utf-8')
        request_lines = send_data.split('\r\n')
        request_line = request_lines[0].split(' ')
        parsed_log['method'] = request_line[0]
        parsed_log['path'] = request_line[1]

    # Extract response status code
    if 'reply' in log:
        reply_line = log['reply'].split(' ')
        parsed_log['status_code'] = int(reply_line[1])

    # Extract server information
    if 'header' in log:
        parsed_log['server'] = log['header']

    return parsed_log