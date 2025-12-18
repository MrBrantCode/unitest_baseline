"""
QUESTION:
Create a function named `create_dict` that constructs a dictionary where every key and word pair from two provided lists (`key_list` and `word_list`) are iteratively duplicated according to the numerical values specified in a third list (`num_list`). The key should reflect an item from `key_list` and its associated word, with repetition dependent on its correspondingly indexed number from `num_list`. The function should take three parameters: `word_list`, `key_list`, and `num_list`, and return the resulting dictionary.
"""

def create_dict(word_list, key_list, num_list):
    result_dict = {}
    for word, key, num in zip(word_list, key_list, num_list):
        result_dict[key] = [word] * num
    return result_dict