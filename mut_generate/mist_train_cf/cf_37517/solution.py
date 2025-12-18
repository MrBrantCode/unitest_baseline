"""
QUESTION:
Create a function `extract_app_config_info(file_paths)` that takes a list of file paths as input and returns a dictionary containing the app name, file name, and the number of GitHub stars for each app configuration class found in the files. The file paths are formatted as `<filename><app_name>/apps.py<gh_stars><num_stars>`, where `<filename>` is the name of the file, `<app_name>` is the name of the Django app, and `<num_stars>` is the number of GitHub stars for the app. The function should construct the configuration class name based on the app name by capitalizing the first letter of each word and appending "Config" to the end.
"""

import re

def extract_app_config_info(file_paths):
    app_config_info = {}
    for path in file_paths:
        match = re.search(r'([^/]+)\/apps.py<gh_stars>(\d+)', path)
        if match:
            app_name = match.group(1)
            num_stars = int(match.group(2))
            file_name = "apps.py"
            config_class_name = ''.join(word.capitalize() or '_' for word in app_name.split('_')) + "Config"
            app_config_info[app_name] = {"app_name": config_class_name, "file_name": file_name, "num_stars": num_stars}
    return app_config_info