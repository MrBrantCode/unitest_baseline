"""
QUESTION:
Create a function called `autodiscover_admins` that takes a list of Python module objects as input and returns a dictionary mapping the module names to the admin classes found within those modules. The function should iterate through the provided modules, inspecting each one for admin classes (identified by having `__module__` attribute equal to the module name and starting with 'Admin'). If an admin class is found within a module, it should be added to the result dictionary with the key being the module name and the value being the admin class.
"""

def autodiscover_admins(modules: list) -> dict:
    result = {}
    for module in modules:
        module_name = module.__name__
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if hasattr(attr, '__module__') and attr.__module__ == module_name and attr_name.startswith('Admin'):
                result[module_name] = attr
    return result