"""
QUESTION:
Create a function named `create_objects` that takes an integer `n` as input and returns a list of objects, where each object is of type `SomeClass`. The function should optimize memory usage by preallocating memory for all objects and reusing that memory in each iteration of the loop, rather than creating a new object every time. Use the `ctypes` module to allocate and manipulate memory directly.
"""

import ctypes

class SomeClass(ctypes.Structure):
    pass

def create_objects(n):
    size = ctypes.sizeof(SomeClass)
    buffer = ctypes.create_string_buffer(n * size)
    objects = []
    for i in range(n):
        obj = SomeClass.from_address(ctypes.addressof(buffer) + i * size)
        objects.append(obj)
    return objects