"""
QUESTION:
Replace the following characters in a string with their corresponding HTML entities: '<' to '&lt;', '>' to '&gt;', "'" to '&apos;', and '"' to '&quot;'. Create a function called `html_entity_parser(input_str)` to accomplish this task.
"""

def html_entity_parser(input_str):
    entity_dict = {'>': '&gt;', 
                   '<': '&lt;', 
                   "'": '&apos;', 
                   '"': '&quot;'}
    return "".join(entity_dict.get(i, i) for i in input_str)