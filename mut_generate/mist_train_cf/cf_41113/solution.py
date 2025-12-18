"""
QUESTION:
Implement a function `call_with` that takes a factory function and keyword arguments as input and returns the rule object created by the factory function. The `call_with` function should dynamically call the factory function with the given keyword arguments. 

Implement the factory functions `span_rule_factory`, `periodic_rule_factory`, and `progressbar_formatter_factory` to create rule objects with specific properties based on the given keyword arguments. The `span_rule_factory` and `periodic_rule_factory` functions should create rule objects with a 'period' property, while the `progressbar_formatter_factory` function should create a rule object with a 'kwargs' property. The names of the rule objects created by `span_rule_factory` and `periodic_rule_factory` should match when given the same keyword arguments.
"""

def call_with(factory, **kwargs):
    return factory(**kwargs)

def span_rule_factory(**kwargs):
    return type('SpanRule', (), {'period': kwargs['period']})()

def periodic_rule_factory(**kwargs):
    return type('PeriodicRule', (), {'period': kwargs['period']})()

def progressbar_formatter_factory(**kwargs):
    return type('ProgressbarFormatter', (), {'kwargs': kwargs})()