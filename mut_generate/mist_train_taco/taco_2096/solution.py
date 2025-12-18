"""
QUESTION:
# Personalized greeting

Create a function that gives a personalized greeting. This function takes two parameters: `name` and `owner`.

Use conditionals to return the proper message:

case | return
--- | ---
name equals owner | 'Hello boss'
otherwise         | 'Hello guest'
"""

def personalized_greeting(name: str, owner: str) -> str:
    return 'Hello boss' if name == owner else 'Hello guest'