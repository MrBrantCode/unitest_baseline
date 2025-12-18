"""
QUESTION:
Write a function `parse_settings(settings_list)` that takes a list of configuration settings in the format "Category-setting_name-setting_property" as input and returns a dictionary where the keys are the categories and the values are lists of tuples containing the setting names and their properties. Each setting's name and property should be separated by a hyphen and a hyphen should separate the category from the setting's name. If a setting has no property, an empty string should be used as the property.
"""

def parse_settings(settings_list):
    settings_dict = {}
    for setting in settings_list:
        category, setting_info = setting.split('-', 1)
        if '-' in setting_info:
            setting_name, setting_property = setting_info.split('-')
        else:
            setting_name, setting_property = setting_info, ''
        if category in settings_dict:
            settings_dict[category].append((setting_name, setting_property))
        else:
            settings_dict[category] = [(setting_name, setting_property)]
    return settings_dict