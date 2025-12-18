"""
QUESTION:
Write a function `handle_prometheus_down` that implements a mechanism to handle cases when the Prometheus data source is down, preventing spam alerts and only notifying that Prometheus is down.
"""

def handle_prometheus_down(prometheus_status):
    """
    This function takes the status of Prometheus as input and returns a boolean indicating whether Prometheus is down.

    Args:
    prometheus_status (bool): The status of Prometheus (True if up, False if down)

    Returns:
    bool: True if Prometheus is down, False otherwise
    """
    return not prometheus_status