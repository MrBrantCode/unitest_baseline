"""
QUESTION:
Design a function called `create_accessible_alert` that takes in a notification type and a vibration pattern, and returns a dictionary containing the alert type, vibration pattern, and a flag to toggle the alert on or off. Ensure the function is flexible enough to incorporate potential improvements in assistive technology. The function should also include a parameter for a color-blind friendly color scheme.
"""

def create_accessible_alert(notification_type, vibration_pattern, color_scheme, alert_on=True):
    """
    Creates a dictionary containing the alert type, vibration pattern, color scheme, and a flag to toggle the alert on or off.

    Args:
        notification_type (str): The type of alert.
        vibration_pattern (str): The vibration pattern for the alert.
        color_scheme (str): A color-blind friendly color scheme.
        alert_on (bool, optional): A flag to toggle the alert on or off. Defaults to True.

    Returns:
        dict: A dictionary containing the alert type, vibration pattern, color scheme, and the alert toggle flag.
    """

    # Create a dictionary with the provided parameters
    alert = {
        'alert_type': notification_type,
        'vibration_pattern': vibration_pattern,
        'color_scheme': color_scheme,
        'alert_on': alert_on
    }

    # Return the created alert dictionary
    return alert