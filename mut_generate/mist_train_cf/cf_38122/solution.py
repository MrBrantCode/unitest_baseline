"""
QUESTION:
Implement a function `hello_world(name, language='English')` that returns a greeting message based on the provided `name` and `language`. The function should support English, Spanish, French, and German languages. If the `name` is not `None`, the function should return a greeting message in the specified language followed by the `name`. If the `name` is `None`, the function should return a greeting message in the specified language followed by "world!". If the language is not supported, the function should default to English.
"""

def hello_world(name, language='English'):
    greetings = {
        'English': 'Hello',
        'Spanish': 'Hola',
        'French': 'Bonjour',
        'German': 'Guten Tag'
    }
    if language in greetings:
        return f'{greetings[language]} {name}' if name is not None else f'{greetings[language]} world!'
    else:
        return f'Hello {name}' if name is not None else 'Hello world!'