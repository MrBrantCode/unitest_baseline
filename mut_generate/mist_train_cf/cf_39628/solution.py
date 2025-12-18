"""
QUESTION:
Create a function `validate_config(c)` that takes a configuration object `c` as input and validates its settings based on the following conditions: 
- `c.GitHubConfig.access_token` is not an empty string
- `c.JupyterApp.answer_yes` is `True`
- `c.LabApp.user_settings_dir` and `c.LabApp.workspaces_dir` are non-empty strings
- `c.NotebookApp.allow_origin` is a non-empty string

The function should return `True` if all conditions are met and `False` otherwise.
"""

def validate_config(c):
    if c.GitHubConfig.access_token == '' or not c.JupyterApp.answer_yes:
        return False
    if c.LabApp.user_settings_dir == '' or c.LabApp.workspaces_dir == '' or c.NotebookApp.allow_origin == '':
        return False
    return True