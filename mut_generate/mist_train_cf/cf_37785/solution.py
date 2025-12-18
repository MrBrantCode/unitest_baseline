"""
QUESTION:
Implement the function `process_response(resp, count, crawler)` that takes a response object `resp`, an integer `count`, and a logger object `crawler` as inputs. The function should process `resp.text` by encoding and decoding it to UTF-8 if it is not empty, log the response headers using `crawler.info(resp.headers)`, and return the processed `resp.text` or incremented `count`. If any errors occur during processing, terminate the parent process using `os.kill()` with the `SIGTERM` signal and return the error message. Ensure the function handles potential errors and exceptions.
"""

import os
import signal

def entrance(resp, count, crawler):
    try:
        if resp.text:
            api_result = resp.text.encode('utf-8', 'ignore').decode('utf-8')
            crawler.info(resp.headers)
        else:
            count += 1
            return count
    except Exception as e:
        os.kill(os.getppid(), signal.SIGTERM)
        return str(e)
    return api_result