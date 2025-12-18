"""
QUESTION:
Create a function called `validate_json_data` that reads JSON data and performs the following operations: 
- It should return the value of the "Name" field.
- It should check if the "Version" field is in the format of a semantic version (e.g., 1.0.0). If not, it should return an error message.
- It should check if the "Dependencies" field is a valid JSON array and if each element in the array is a valid semantic version. If any of the dependencies are not valid, it should return an error message with the index of the invalid dependency.
"""

import json
import re

def validate_json_data(json_data):
    try:
        # Load JSON data
        data = json.loads(json_data)
        
        # Get the value of the "Name" field
        name = data['Name']
        
        # Validate the "Version" field
        version = data['Version']
        if not re.match(r'^\d+\.\d+\.\d+$', version):
            return f"Error: Invalid version format"
        
        # Check "Dependencies" field
        dependencies = data['Dependencies']
        if not isinstance(dependencies, list):
            return "Error: Dependencies should be a JSON array"
        
        for index, dependency in enumerate(dependencies):
            if not re.match(r'^\d+\.\d+\.\d+$', dependency):
                return f"Error: Invalid version format for dependency at index {index}"
        
        return name
    
    except (KeyError, ValueError) as e:
        return f"Error: {str(e)}"