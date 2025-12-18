"""
QUESTION:
Write a function named `process_data` that takes a stream of data as input and logs the progress after every 1000 rows processed. The logging should include the number of rows processed so far. The function should also return the total number of rows processed. Assume that the data stream is an iterable object that yields data one row at a time.
"""

import logging

def process_data(stream):
    row_count = 0
    for data in stream:
        # Process the data here
        # ...
        row_count += 1
        if row_count % 1000 == 0:
            logging.info("Processed {} rows".format(row_count))
    return row_count