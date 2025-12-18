"""
QUESTION:
Implement a function named `lazy` that takes the name of a Python module as a string and returns a lazy-loaded module object. The function should delay the actual import of the module until its attributes are accessed for the first time. The `lazy` function should handle attribute access and assignment using the `__getattr__` and `__setattr__` methods. The function should also provide a string representation of the module using the `__repr__` method, indicating whether the module is loaded or not.
"""

def lazy(module_name):
    class LazyModule:
        def __init__(self, module_name):
            self.module_name = module_name
            self.module = None

        def __getattr__(self, attr):
            if self.module is None:
                self.module = __import__(self.module_name)
            return getattr(self.module, attr)

        def __setattr__(self, attr, value):
            if attr != 'module' and attr != 'module_name':
                if self.module is None:
                    self.module = __import__(self.module_name)
                setattr(self.module, attr, value)
            else:
                super().__setattr__(attr, value)

        def __repr__(self):
            if self.module is None:
                return f"<LazyModule '{self.module_name}' (not loaded)>"
            else:
                return f"<LazyModule '{self.module_name}' (loaded)>"

    return LazyModule(module_name)