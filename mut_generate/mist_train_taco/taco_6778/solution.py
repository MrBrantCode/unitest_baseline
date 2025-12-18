"""
QUESTION:
Create a method `sayHello`/`say_hello`/`SayHello` that takes as input a name, city, and state to welcome a person. Note that `name` will be an array consisting of one or more values that should be joined together with one space between each, and the length of the `name` array in test cases will vary.

Example:

```python
say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
```

This example will return the string `Hello, John Smith! Welcome to Phoenix, Arizona!`
"""

def say_hello(name, city, state):
    """
    Generates a welcome message for a person based on their name, city, and state.

    Parameters:
    - name (list of str): A list of strings representing the parts of the person's name.
    - city (str): A string representing the city.
    - state (str): A string representing the state.

    Returns:
    - str: A formatted welcome message.
    """
    return 'Hello, {}! Welcome to {}, {}!'.format(' '.join(name), city, state)