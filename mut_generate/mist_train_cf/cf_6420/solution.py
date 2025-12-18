"""
QUESTION:
Write a function `json_to_dataframe` that takes a JSON object as input and converts it into a Pandas dataframe, handling complex JSON structures with multiple nested levels, including lists, dictionaries, and various data types. The function should efficiently handle large JSON objects and convert them into a structured dataframe while preserving the integrity of the data, including missing values, NaN values, duplicate keys, datetime objects, unicode characters, and custom data types.
"""

import pandas as pd

def json_to_dataframe(json_obj):
    def process_json(json_obj, parent_key='', data_dict={}):
        if isinstance(json_obj, dict):
            for k,v in json_obj.items():
                new_key = parent_key + '_' + k if parent_key else k
                process_json(v, new_key, data_dict)
        elif isinstance(json_obj, list):
            for i,v in enumerate(json_obj):
                new_key = parent_key + '_index_' + str(i) if parent_key else 'index_' + str(i)
                process_json(v, new_key, data_dict)
        else:
            data_dict[parent_key] = json_obj

        return data_dict
    
    data_dict = process_json(json_obj)
    df = pd.DataFrame.from_dict(data_dict, orient='index')
    return df