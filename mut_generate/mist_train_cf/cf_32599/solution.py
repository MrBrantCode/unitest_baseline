"""
QUESTION:
Create a function `extract_app_info` that takes a JSON object as input and extracts the following key-value pairs: 
- "kitBuildNumber" 
- "kitBuildType" 
- "appVer" 
- "app_debuggable" (default to "0" if not present) 
- "appBuild" 
- "osVer" 
- "osApiLev" (default to -1 if not present) 

Store these key-value pairs in a suitable data structure for further processing and manipulation.
"""

import json

def extract_app_info(json_obj):
    app_info = {
        "kitBuildNumber": json_obj.get("kitBuildNumber"),
        "kitBuildType": json_obj.get("kitBuildType"),
        "appVer": json_obj.get("appVer"),
        "app_debuggable": json_obj.get("app_debuggable", "0"),
        "appBuild": json_obj.get("appBuild"),
        "osVer": json_obj.get("osVer"),
        "osApiLev": json_obj.get("osApiLev", -1)
    }
    return app_info