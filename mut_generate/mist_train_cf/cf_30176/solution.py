"""
QUESTION:
Write a function `parse_callbacks` that takes in three parameters: `callback_config` (dict), `trainer_config` (dict), and `thelper_utils` (module). The function should extract and process configuration parameters for "user_callback" and "display_callback" from `callback_config`, instantiate corresponding callback objects using provided configuration parameters, and return a dictionary containing the instantiated callback objects. The function should use `thelper_utils.get_key_def` to safely retrieve nested dictionary values and `thelper_utils.train.utils.PredictionCallback` to create prediction callbacks. If a callback key is not present in `callback_config`, its corresponding callback object should not be instantiated.
"""

def parse_callbacks(callback_config, trainer_config, thelper_utils):
    instantiated_callbacks = {}
    
    if "user_callback" in callback_config:
        user_callback_kwargs_keys = callback_config["user_callback"]
        user_callback_kwargs = thelper_utils.get_key_def(user_callback_kwargs_keys, trainer_config, {})
        instantiated_callbacks["user_callback"] = thelper_utils.train.utils.PredictionCallback(user_callback_kwargs)
    
    if "display_callback" in callback_config:
        display_callback_kwargs_keys = callback_config["display_callback"]
        display_callback_kwargs = thelper_utils.get_key_def(display_callback_kwargs_keys, trainer_config, {})
        instantiated_callbacks["display_callback"] = thelper_utils.train.utils.PredictionCallback(display_callback_kwargs)
    
    return instantiated_callbacks