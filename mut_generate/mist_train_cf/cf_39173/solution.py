"""
QUESTION:
Implement the `format` and `dump` methods for the `MathModel` class.

The `format` method should return a string representation of the model in the format 'name(parameters)', where 'name' is the name of the model and 'parameters' is a comma-separated list of the model's parameters.

The `dump` method should return a dictionary containing the model's attributes, including 'name', 'params', 'condition', 'variate', and 'ode'. The 'params' value should be a list of the dumped parameters, and the 'condition', 'variate', and 'ode' values should be the dumped representations of the corresponding attributes.

Assume that the 'parameters', 'condition', 'variate', and 'ode' attributes have a 'dump' method that returns their dumped representations.
"""

def format_math_model(model):
    """Returns a string representation of the model in the format 'name(parameters)'"""
    params_str = ', '.join(str(param) for param in model.parameters)
    return '{}({})'.format(model.name, params_str)

def dump_math_model(model):
    """Returns a dictionary containing the model's attributes"""
    return dict(name=model.name,
                params=[param.dump() for param in model.parameters],
                condition=model.condition.dump(),
                variate=model.variate.dump(),
                ode=model.ode.dump())