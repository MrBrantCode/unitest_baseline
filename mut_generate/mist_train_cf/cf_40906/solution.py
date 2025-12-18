"""
QUESTION:
Implement a function `handle_async_futures` that takes a list of `asyncio.Future` objects and a default value. The function should return the result of the first successful future. If all futures fail, it should return the default value if provided, otherwise it should return the result of the first failed future. If no default value is provided and all futures fail, it should return None.
"""

import asyncio

_no_value = object()

def handle_async_futures(futures, default=_no_value):
    first_future = None
    for future in futures:
        try:
            result = future.result()
            return result
        except Exception as e:
            if first_future is None:
                first_future = future
            pass

    if default is not _no_value:
        return default

    if first_future is not None:
        return first_future.result()

    return None