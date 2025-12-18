"""
QUESTION:
Write a function ```unpack()``` that unpacks a ```list``` of elements that can contain objects(`int`, `str`, `list`, `tuple`, `dict`, `set`) within each other without any predefined depth, meaning that there can be many levels of elements contained in one another.

Example:

```python
unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]) == [None, 1, 2, 3, 'foo', 'bar']
```

Note: you don't have to bother about the order of the elements, especially when unpacking a `dict` or a `set`. Just unpack all the elements.
"""

from collections.abc import Iterable

def unpack_nested_elements(iterable):
    result = []
    for element in iterable:
        if isinstance(element, dict):
            element = unpack_nested_elements(element.items())
        elif isinstance(element, str):
            element = [element]
        elif isinstance(element, Iterable) and not isinstance(element, (str, bytes)):
            element = unpack_nested_elements(element)
        else:
            element = [element]
        result.extend(element)
    return result