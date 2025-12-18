"""
QUESTION:
Create a function `get_average_response_time(line_id)` that calculates the average response time of a bot to send a message to a specified LINE ID. The function should connect to a SQLite database 'eip.db' and query the EIP_MessageDetail table to retrieve the durations of all messages sent to the specified LINE ID. If no messages are found, return None. 

Additionally, modify the function that inserts messages into the EIP_MessageDetail table to record the time it takes to generate and insert the message. Store the duration in a new column 'Duration' in the EIP_MessageDetail table. Assume the EIP_MessageDetail table already exists and has columns for MessageId, LineId, and MessageContent.
"""

import sqlite3

def get_average_response_time(line_id):
    # Connect to SQLite database
    conn = sqlite3.connect('eip.db')
    c = conn.cursor()

    # Query EIP_MessageDetail table for messages sent to specified LINE ID
    c.execute("SELECT Duration FROM EIP_MessageDetail WHERE LineId = ?", (line_id,))
    durations = c.fetchall()

    # Calculate average duration
    if len(durations) > 0:
        average_duration = sum(duration[0] for duration in durations) / len(durations)
    else:
        average_duration = None

    # Close connection and return result
    conn.close()
    return average_duration