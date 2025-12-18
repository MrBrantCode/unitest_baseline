"""
QUESTION:
Create a function `get_landmark_info` that retrieves and returns information about a specific landmark. The function should take in two parameters: `landmark_name` and `info_type`, where `info_type` can be 'address', 'phone', or 'general info'. The function should return the requested information as a string. 

Assume that you have access to a dictionary `landmarks` that stores the information about different landmarks. The keys of the dictionary are the landmark names, and the values are another dictionary containing the 'address', 'phone', and 'description' of the landmark.
"""

def get_landmark_info(landmark_name, info_type):
    landmarks = {
        "Statue of Liberty": {
            "address": "Liberty Island, New York, NY 10004, United States",
            "phone": "+1 212-363-3200",
            "description": "The Statue of Liberty was a gift from France in 1886. It serves as a symbol of freedom and democracy. It's located on Liberty Island in New York Harbor."
        }
    }
    
    if landmark_name not in landmarks:
        return "Landmark not found."
    
    if info_type == 'address':
        return landmarks[landmark_name]['address']
    elif info_type == 'phone':
        return landmarks[landmark_name]['phone']
    elif info_type == 'general info':
        return landmarks[landmark_name]['description']
    else:
        return "Invalid info type."