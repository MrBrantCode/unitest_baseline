"""
QUESTION:
Create a function `collect_yaml_config` that takes a dictionary `config` as input and returns a pandas DataFrame. The function should exclude keys 'policies' and 'seed' from the input dictionary, create a new dictionary with the remaining keys and their corresponding values, and then convert this dictionary into a DataFrame.
"""

import pandas as pd

def collect_yaml_config(config: dict) -> pd.DataFrame:
    keys = list(filter(lambda key: key not in ['policies', 'seed'], config.keys()))
    global_setting = {key: config[key] for key in keys}
    return pd.DataFrame(list(global_setting.items()), columns=['key', 'value'])