"""
QUESTION:
Create a Python class `InventoryManager` that manages inventory locales in a software system. The class should have two methods: `get_locales_set` and `get_locale_lang_tuple`. The `get_locales_set` method returns a tuple of three sets: active locales, inactive locales, and aliases. The `get_locale_lang_tuple` method returns a dictionary mapping locales to their corresponding languages. The class should be initialized with predefined sets of active locales, inactive locales, and aliases. The predefined active locales are 'en', 'fr', and 'de', the predefined inactive locale is 'es', and the predefined aliases are 'en_US': 'en', 'fr_FR': 'fr', 'de_DE': 'de', and 'es_ES': 'es'. The locale to language mapping should include 'en': 'English', 'fr': 'French', 'de': 'German', and 'es': 'Spanish'.
"""

def inventory_manager(active_locales, inactive_locales, aliases, locale_lang_map):
    def get_locales_set():
        return active_locales, inactive_locales, aliases

    def get_locale_lang_tuple():
        return locale_lang_map

    return get_locales_set, get_locale_lang_tuple


active_locales = {'en', 'fr', 'de'}
inactive_locales = {'es'}
aliases = {'en_US': 'en', 'fr_FR': 'fr', 'de_DE': 'de', 'es_ES': 'es'}
locale_lang_map = {'en': 'English', 'fr': 'French', 'de': 'German', 'es': 'Spanish'}

get_locales_set, get_locale_lang_tuple = inventory_manager(active_locales, inactive_locales, aliases, locale_lang_map)