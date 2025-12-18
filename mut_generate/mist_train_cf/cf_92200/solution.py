"""
QUESTION:
Write a Python function called `custom_format()` that takes in three arguments: `name`, `age`, and `city`. The function should return a formatted string in the following pattern: "Hello, my name is [name]. I am [age] years old, and I live in [city]." without using the `str.format()` method.
"""

def custom_format(name, age, city):
    return "Hello, my name is %s. I am %d years old, and I live in %s." % (name, age, city)