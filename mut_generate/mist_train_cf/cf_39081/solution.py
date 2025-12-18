"""
QUESTION:
Implement the `system_groupname_from_groupid` function, which takes a non-negative integer `groupid` as input and returns its corresponding system group name. The function should use the following predefined group ID mappings: {0: "admin", 1: "users", 2: "guests"}. If the `groupid` does not match any known group, return "Unknown Group".
"""

def system_groupname_from_groupid(groupid):
    group_mapping = {
        0: "admin",
        1: "users",
        2: "guests"
    }
    return group_mapping.get(groupid, "Unknown Group")