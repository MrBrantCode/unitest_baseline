"""
QUESTION:
Create a function named `parse_json_objects` that takes a list of JSON objects as input and returns a dictionary. The dictionary should include only the "name", "age", and "hobbies" fields from the JSON objects. The "name" field should be in uppercase. The function should validate that the "age" field is a positive integer and that the "hobbies" field is a list of strings. It should also remove any duplicate values from the "hobbies" field before adding them to the dictionary. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def parse_json_objects(json_objects):
    parsed_dict = {}
    for obj in json_objects:
        if "name" in obj and "age" in obj and "hobbies" in obj:
            name = obj["name"].upper()
            age = obj["age"]
            hobbies = obj["hobbies"]

            if isinstance(age, int) and age > 0 and isinstance(hobbies, list) and all(isinstance(hobby, str) for hobby in hobbies):
                unique_hobbies = list(set(hobbies))
                parsed_dict[name] = {
                    "age": age,
                    "hobbies": unique_hobbies
                }

    return parsed_dict