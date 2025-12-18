"""
QUESTION:
Write a function `flatten_dict` that can handle nested dictionaries and lists of any level, and another function `calculate_average_age` to calculate the average age of a person's friends. The function `flatten_dict` should take a dictionary `d` and a prefix as parameters, and return a flattened dictionary. The function `calculate_average_age` should take a row of a Pandas DataFrame as input and return the average age of the person's friends.
"""

def flatten_dict(d, prefix=''):
    flat_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, prefix + key + '_'))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    flat_dict.update(flatten_dict(item, prefix + key + '_' + str(i) + '_'))
        else:
            flat_dict[prefix + key] = value
    return flat_dict

def calculate_average_age(row):
    friend_cols = [col for col in row.index if col.startswith('friends_') and col.endswith('age')]
    friend_ages = [row[col] for col in friend_cols if not pd.isnull(row[col])]
    if friend_ages:
        return sum(friend_ages) / len(friend_ages)
    else:
        return None