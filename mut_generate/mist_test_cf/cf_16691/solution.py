"""
QUESTION:
Write a function `manipulate_json` that takes a JSON string as input, validates that it has the required fields ("name", "age", "email", "address", "hobbies", "education", "friends"), calculates the total number of friends, adds a new friend to the "friends" array, updates the age of the person with the name "John Doe" to 26, and returns the updated JSON object as a string. The function should handle error cases such as missing fields or incorrect data types.
"""

import json

def manipulate_json(json_str):
    try:
        # Parse the JSON string into a Python dictionary
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return "Invalid JSON format"

    # Check if all required fields are present
    required_fields = ["name", "age", "email", "address", "hobbies", "education", "friends"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return f"Missing fields: {', '.join(missing_fields)}"

    # Calculate the total number of friends
    num_friends = len(data["friends"])

    # Add a new friend
    new_friend = {
        "name": "Sarah Brown",
        "age": 26,
        "email": "sarahbrown@example.com"
    }
    data["friends"].append(new_friend)

    # Update John Doe's age
    for friend in data["friends"]:
        if friend["name"] == "John Doe":
            friend["age"] = 26
            break

    # Return the updated JSON object
    return json.dumps(data, indent=2)