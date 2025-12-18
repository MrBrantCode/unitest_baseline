"""
QUESTION:
Implement the function `dereference_config(cfg)` that takes a configuration object `cfg` as input. `cfg` is a dictionary that may contain nested structures, including lists and dictionaries. The dictionary contains references to other parts of the configuration, represented as strings enclosed within double curly braces `{{}}`. The function should return a new configuration object with all references replaced by their actual values.
"""

def dereference_config(cfg):
    def resolve_reference(ref, config):
        parts = ref.split('.')
        value = config
        for part in parts:
            value = value[part]
        return value

    def replace_references(obj, config):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, str) and value.startswith("{{") and value.endswith("}}"):
                    obj[key] = resolve_reference(value[2:-2], config)
                else:
                    replace_references(value, config)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, str) and item.startswith("{{") and item.endswith("}}"):
                    obj[i] = resolve_reference(item[2:-2], config)
                else:
                    replace_references(item, config)

    dereferenced_cfg = cfg.copy()
    replace_references(dereferenced_cfg, dereferenced_cfg)
    return dereferenced_cfg