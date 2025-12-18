"""
QUESTION:
Implement a function `format_user_info(content, template)` that takes a dictionary `content` and a string template, and returns the formatted string according to the template. The `content` dictionary has the structure `{"desc": {"user_profile": {"info": {"uname": string}}, "dynamic_id_str": string}}`. The template string contains placeholders for the extracted information enclosed in curly braces, such as `{username}` and `{id}`. If the `content` dictionary does not contain all the expected keys, return an empty string.
"""

def format_user_info(content, template):
    try:
        formatted_string = template.format(
            username=content["desc"]["user_profile"]["info"]["uname"],
            id=content["desc"]["dynamic_id_str"]
        )
        return formatted_string
    except KeyError:
        return ""