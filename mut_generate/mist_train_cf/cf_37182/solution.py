"""
QUESTION:
Create a Python function `process_database_config` that takes a dictionary `config` as input and returns a string. The function should check if the 'default' key exists in the dictionary and if its 'ENGINE' value is set to 'django.db.backends.postgresql_psycopg2'. If both conditions are met, the function should return the 'NAME' value of the 'default' configuration. If not, it should return an empty string.
"""

def process_database_config(config: dict) -> str:
    if 'default' in config:
        default_config = config['default']
        if 'ENGINE' in default_config and default_config['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
            return default_config['NAME']
    return ""