"""
QUESTION:
Create a function named `join_data_sets` that joins two data sets based on the `user_id`. The function should take two parameters: `data_set1` and `data_set2`, where each data set is a list of dictionaries. `data_set1` contains `user_id`, `firstname`, and `age`, and `data_set2` contains `user_id` and `lastname`. The function should return a new data set with `firstname`, `lastname`, `age`, and `user_id`, where the `age` is an integer between 0 and 100. The time complexity of the solution should be O(n), where n is the length of the longer input data set, and the space complexity should be O(n), where n is the length of the output data set.
"""

def join_data_sets(data_set1, data_set2):
    # Create a dictionary to store the combined data
    combined_data = {}

    # Iterate over the first data set and add firstname and age to the dictionary
    for row in data_set1:
        user_id = row["user_id"]
        firstname = row["firstname"]
        age = row["age"]
        combined_data[user_id] = {"firstname": firstname, "age": age}

    # Iterate over the second data set and add lastname to the dictionary
    for row in data_set2:
        user_id = row["user_id"]
        lastname = row["lastname"]
        # Check if the user_id is already present in the dictionary
        if user_id in combined_data:
            combined_data[user_id]["lastname"] = lastname

    # Convert the dictionary into a list of dictionaries
    result = []
    for user_id, data in combined_data.items():
        if "lastname" in data:
            result.append({"user_id": user_id, "firstname": data["firstname"], "lastname": data["lastname"], "age": data["age"]})

    return result