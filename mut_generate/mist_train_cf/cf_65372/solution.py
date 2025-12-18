"""
QUESTION:
Disable Gyroscope for video_360 Plugin

Write a function to disable the gyroscope sensing in the `video_360` plugin, which does not provide an API to do so. The solution should prevent the plugin from reading and updating gyroscope values, effectively "freezing" the sensor readings. Note that modifying the plugin requires knowledge of Kotlin/Java for Android and Swift/ObjC for iOS.
"""

def disable_gyroscope(gyroscope_values):
    """
    Simulate disabling the gyroscope by freezing its values.
    
    Args:
        gyroscope_values (list): The list of gyroscope values.
    
    Returns:
        list: The frozen gyroscope values.
    """
    # Freeze the gyroscope values by returning the same values
    return gyroscope_values