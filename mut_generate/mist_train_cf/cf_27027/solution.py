"""
QUESTION:
Write a function `parse_bot_commands(json_data)` that takes a JSON object `json_data` as input and processes any bot commands present in the data. The function should return a list of bot commands extracted from the JSON data. If no bot commands are found or if the JSON data does not conform to the expected structure, the function should return an empty list. The JSON data structure is expected to contain a "message" key with an "entities" list, where each entity has a "type" key that may be "bot_command", and an "offset" and "length" key to extract the command from the "text" key in the "message". The function should handle cases where the JSON data may not contain the expected structure or entities.
"""

def parse_bot_commands(json_data):
    bot_commands = []
    try:
        if "message" in json_data and "entities" in json_data["message"]:
            for entity in json_data["message"]["entities"]:
                if "type" in entity and entity["type"] == "bot_command":
                    bot_commands.append(json_data["message"]["text"][entity["offset"]:entity["offset"] + entity["length"]])
    except KeyError:
        pass
    return bot_commands