"""
QUESTION:
Write a Python function `extract_function_info(f)` that takes a function `f` as input and returns a dictionary containing the following information: 
- `args`: a list of the function's positional arguments
- `varargs`: the name of the variable that collects positional arguments beyond the formal parameter list
- `varkw`: the name of the variable that collects keyword arguments not explicitly named in the formal parameter list
- `defaults`: a tuple containing the default values of the function's positional arguments
- `kwonlyargs`: a list of keyword-only arguments
- `kwonlydefaults`: a dictionary containing the default values of the function's keyword-only arguments
- `annotations`: a dictionary containing the type annotations of the function's arguments

The function should use the `inspect` module to retrieve the full argument specification of the input function.
"""

import inspect

def extract_function_info(f):
    info = {}
    argspec = inspect.getfullargspec(f)
    
    info['args'] = argspec.args
    info['varargs'] = argspec.varargs
    info['varkw'] = argspec.varkw
    info['defaults'] = argspec.defaults
    info['kwonlyargs'] = argspec.kwonlyargs
    info['kwonlydefaults'] = argspec.kwonlydefaults
    info['annotations'] = getattr(f, '__annotations__', {})
    
    return info