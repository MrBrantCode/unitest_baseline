"""
QUESTION:
Remove the preference tag from the AndroidManifest.xml file and define the minSdkVersion in the build.gradle file instead. Write a function `set_min_sdk_version` that takes the `build_gradle_dict` as input and returns the updated `build_gradle_dict` with the `minSdkVersion` set to 22. The `build_gradle_dict` is a dictionary containing the keys 'compileSdkVersion', 'defaultConfig', and other configuration settings.

Restrictions: The input `build_gradle_dict` should contain the key 'defaultConfig'. The function should return the updated `build_gradle_dict` with the `minSdkVersion` set to 22.
"""

def set_min_sdk_version(build_gradle_dict):
    """
    Updates the build_gradle_dict to set the minSdkVersion to 22.

    Args:
        build_gradle_dict (dict): A dictionary containing the keys 'compileSdkVersion', 'defaultConfig', and other configuration settings.

    Returns:
        dict: The updated build_gradle_dict with the minSdkVersion set to 22.
    """
    if 'defaultConfig' in build_gradle_dict:
        build_gradle_dict['defaultConfig']['minSdkVersion'] = 22
    return build_gradle_dict