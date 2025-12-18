"""
QUESTION:
Write a function `parse_db_instance_string(db_instance_str)` that takes a string representing a database instance as input and returns a dictionary containing the parsed information. The string has the following format: 
```
# DBINSTANCES <Number of Instances> <Multi-AZ Deployment> <Availability Zone> <Backup Retention Period> <DB Instance Class> <Instance ID> <Instance Status> <DB Name> <Engine> <Engine Version> <Instance Create Time> <License Model> <Master Username> <Multi-AZ> <Preferred Maintenance Window> <Backup Window> <Publicly Accessible>
```
The output dictionary should include the following keys and their corresponding values:
- "Number of Instances": <Number of Instances>
- "Multi-AZ Deployment": <Multi-AZ Deployment>
- "Availability Zone": <Availability Zone>
- "Backup Retention Period": <Backup Retention Period>
- "DB Instance Class": <DB Instance Class>
- "Instance ID": <Instance ID>
- "Instance Status": <Instance Status>
- "DB Name": <DB Name>
- "Engine": <Engine>
- "Engine Version": <Engine Version>
- "Instance Create Time": <Instance Create Time>
- "License Model": <License Model>
- "Master Username": <Master Username>
- "Multi-AZ": <Multi-AZ>
- "Preferred Maintenance Window": <Preferred Maintenance Window>
- "Backup Window": <Backup Window>
- "Publicly Accessible": <Publicly Accessible>

Note that the function should return `None` if the input string does not match the expected format.
"""

import re

def parse_db_instance_string(db_instance_str):
    pattern = r'# DBINSTANCES (\d+) (\w+) (\S+) (\d+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\w+) (\S+) (\S+) (\w+)'
    match = re.match(pattern, db_instance_str)
    if match:
        keys = ["Number of Instances", "Multi-AZ Deployment", "Availability Zone", "Backup Retention Period", "DB Instance Class",
                "Instance ID", "Instance Status", "DB Name", "Engine", "Engine Version", "Instance Create Time", "License Model",
                "Master Username", "Multi-AZ", "Preferred Maintenance Window", "Backup Window", "Publicly Accessible"]
        return dict(zip(keys, match.groups()))
    else:
        return None