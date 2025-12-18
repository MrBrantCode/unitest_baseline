"""
QUESTION:
Implement a function `save_config_path` that takes a parameter `resource` and returns the absolute path where the configuration for that resource should be saved according to the XDG Base Directory Specification. 

The function should follow these rules: 
1. If `$XDG_CONFIG_HOME` is set, return the absolute path to the resource's configuration file within this directory.
2. If `$XDG_CONFIG_HOME` is not set, check each directory in `$XDG_CONFIG_DIRS` in order and return the absolute path to the resource's configuration file in the first matching directory.
3. If the resource's configuration file is not found in any of the above directories, return the absolute path to the resource's configuration file within a default directory in the user's home directory (`~/.config/resource`).
"""

import os

def save_config_path(resource):
    xdg_config_home = os.environ.get('XDG_CONFIG_HOME')
    if xdg_config_home:
        return os.path.join(xdg_config_home, resource)
    
    xdg_config_dirs = os.environ.get('XDG_CONFIG_DIRS')
    if xdg_config_dirs:
        for directory in xdg_config_dirs.split(':'):
            config_path = os.path.join(directory, resource)
            if os.path.exists(config_path):
                return config_path
    
    return os.path.join(os.path.expanduser('~'), '.config', resource)