"""
QUESTION:
Create a function `trace` that can be used as a decorator to trace the execution of recursive and mutually recursive functions. The function should have the ability to limit the depth of recursion traced and display the trace on the screen. The function should also handle cases where the specified depth limit is reached. The function should work with both recursive and mutually recursive functions.
"""

indent_step = 2
depth_limit = -1

def trace(func):
    if hasattr(func, 'tracing'):
        return func

    def wrapped(*args, **kwargs):
        call = ', '.join(
            [repr(a) for a in args] +
            [f'{k}={v!r}' for k, v in kwargs.items()]
        )
        depth = getattr(wrapped, 'depth', -indent_step)
        if depth//indent_step < depth_limit or depth_limit == -1:
            wrapped.depth = depth + indent_step
            print(f'{" "*depth}>{func.__name__}({call})')
            result = func(*args, **kwargs)
            print(f'{" "*depth}< {result}')
            wrapped.depth = depth
        else:
            result = "***DEPTH LIMIT REACHED***"
        return result
    
    wrapped.tracing = True
    return wrapped