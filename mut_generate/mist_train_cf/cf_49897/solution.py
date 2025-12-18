"""
QUESTION:
Write a function `add_mark_up` that takes a string `text` and a variable number of string `tags` as input, and returns a string with the input `text` wrapped in the input `tags`. The tags should be nested in the order they are provided, with the first tag being the innermost. For example, `add_mark_up('Hello World!', 'tag')` should return `'<tag>Hello World!</tag>'`, and `add_mark_up('Hello World!', 'tag', 'Greet')` should return `'<Greet><tag>Hello World!</tag></Greet>'`. The function should not have any restrictions on the number of tags that can be provided.
"""

def add_mark_up(text: str, *tags: str) -> str:
    for tag in tags[::-1]:
        text = '<' + tag + '>' + text +  '</' + tag + '>'
    return text