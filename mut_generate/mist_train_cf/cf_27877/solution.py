"""
QUESTION:
Write a function `parse_video_info` that takes a string `video_name` (1 <= len(video_name) <= 1000) consisting of alphanumeric characters, spaces, and square brackets as input. The string contains a video title followed by properties enclosed within square brackets and separated by a single space. Each property is in the format "key=value". Return a dictionary containing the video title and its properties, where the keys of the dictionary are "title" for the video title and "properties" for the properties.
"""

def parse_video_info(video_name: str) -> dict:
    title, properties_str = video_name.split("[")
    title = title.strip()
    properties_str = properties_str.rstrip("]")
    properties = properties_str.split()
    properties_dict = {}
    for prop in properties:
        key, value = prop.split("=")
        properties_dict[key] = value
    return {'title': title, 'properties': properties_dict}