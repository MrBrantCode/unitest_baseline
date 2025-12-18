"""
QUESTION:
Create a function `parse_user_agent(user_agent: str) -> dict` that takes a user-agent string as input and returns a dictionary containing the browser name, version, and the operating system. The function should handle different user-agent strings and extract the information accurately. The returned dictionary should have the structure `{"browser": str, "version": str, "os": str}`.
"""

import re

def parse_user_agent(user_agent: str) -> dict:
    browser_info = re.search(r'(\w+)\/([\d.]+)', user_agent)
    os_info = re.search(r'\((.*?)\)', user_agent)

    browser = browser_info.group(1)
    version = browser_info.group(2)
    os = os_info.group(1).split(';')[0]

    return {
        "browser": browser,
        "version": version,
        "os": os
    }