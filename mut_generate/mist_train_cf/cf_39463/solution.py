"""
QUESTION:
Write a function called `generate_jupyter_config` that takes two parameters: `module` and `ports`. The `module` is a dictionary containing the keys "name", "description", "logo-url", "subtype", "path", and "parent-path". The `ports` is a list of dictionaries, each containing the keys "protocol" and "target-port". The function should return a dictionary representing the Jupyter Notebook deployment configuration. The configuration dictionary should include all the keys from the `module` dictionary, the `ports` list, and additional keys "urls" and "restart-policy". The "urls" key should contain a list with a single list element containing the string "jupyter" and a URL string in the format "https://${hostname}:${tcp.{target-port}}/?token=${access-token}". The "restart-policy" key should contain a dictionary with a single key "condition" and value "any".
"""

def generate_jupyter_config(module, ports):
    jupyter_config = {
        "name": module["name"],
        "description": module["description"],
        "logo-url": module["logo-url"],
        "subtype": module["subtype"],
        "path": module["path"],
        "parent-path": module["parent-path"],
        "ports": ports,
        "urls": [["jupyter", f"https${{hostname}}:${{tcp.{ports[0]['target-port']}}}/?token=${{access-token}}"]],
        "restart-policy": {"condition": "any"}
    }
    return jupyter_config