"""
QUESTION:
Implement a Python function `monitor_node_status` that takes a `node_name` and a `default_wait_time` as input and returns a message indicating the status of the boot-up and detection processes of a computing node. The function should check the boot-up status of the node using the `_checkNodeBootSuccess` method and log an informational message if successful. Then, it should check the detection agent status using the `_checkDetectionAgent` method and append a failure message if the detection agent is not successful. The function should return the overall status message. Assume that the `_checkNodeBootSuccess` and `_checkDetectionAgent` methods are implemented elsewhere and are available for use.
"""

import logging

def monitor_node_status(node_name, default_wait_time, _checkNodeBootSuccess, _checkDetectionAgent):
    message = ""
    boot_up = _checkNodeBootSuccess(node_name, default_wait_time)
    if boot_up:
        message += "Start node success. The node is %s." % node_name
        logging.info(message)
        detection = _checkDetectionAgent(node_name, default_wait_time)
        if not detection:
            message += " Detection agent in computing node is fail."
    return message