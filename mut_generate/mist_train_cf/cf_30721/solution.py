"""
QUESTION:
Create a function named `validate_database_config` that takes a dictionary representing the database configuration as input. The function should check the following conditions:
- The dictionary contains the key 'default' and the 'default' dictionary contains the key 'ENGINE' with the value 'django.db.backends.sqlite3'.
- The 'default' dictionary contains the key 'NAME' with a non-empty string value.
- If the 'default' dictionary contains the keys 'USER', 'PASSWORD', 'HOST', and 'PORT', their values should be either empty strings or non-empty strings. 
Return True if all conditions are met; otherwise, return False.
"""

def validate_database_config(config):
    if 'default' in config and 'ENGINE' in config['default'] and config['default']['ENGINE'] == 'django.db.backends.sqlite3' and 'NAME' in config['default'] and config['default']['NAME']:
        if all(key in config['default'] for key in ['USER', 'PASSWORD', 'HOST', 'PORT']):
            if all(isinstance(config['default'][key], str) for key in ['USER', 'PASSWORD', 'HOST', 'PORT']):
                return True
            else:
                return False
        else:
            return True
    else:
        return False