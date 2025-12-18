"""
QUESTION:
Implement the `AuthConfig` class and the `get_config`, `register_config`, and `register_plugin_name` functions to support the registration and retrieval of authentication configuration settings. 

The `AuthConfig` class should have an initializer that accepts a dictionary of settings. The `get_config` function should take a configuration class as an argument and return an instance of the class with some default settings. The `register_config` function should take an instance of the `AuthConfig` class as an argument and return a reference to the configuration. The `register_plugin_name` function should take a string representing the plugin name as an argument and return a reference to the plugin.

Assume a simple dictionary of settings for demonstration purposes. Do not consider fetching settings from a database or a configuration file.
"""

class AuthConfig:
    def __init__(self, settings):
        self.settings = settings

def get_auth_config(config_class):
    return config_class({'username': 'admin', 'password': 'secretpassword'})

def register_auth_config(config_instance):
    return config_instance

def register_auth_plugin_name(plugin_name):
    return plugin_name