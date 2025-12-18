"""
QUESTION:
Create a Python decorator named `addmeth` to dynamically register methods of a class, along with a class named `OrderedMethods`. The `addmeth` decorator should assign an `order` attribute to each registered method based on its definition order. The `OrderedMethods` class should execute these registered methods in the order of their `order` attribute. The registered methods should be added to the `OrderedMethods` instance manually.
"""

def addmeth(func):
    if not hasattr(func, 'order'):
        func.order = 0
    return func

class OrderedMethods:
    def __init__(self):
        self.methods = []

    def add_method(self, method):
        self.methods.append(method)

    def execute_methods(self):
        for method in sorted(self.methods, key=lambda x: x.order):
            method()