"""
QUESTION:
Create a function `create_template_file(title)` that generates a template file with the given title. The template file should be in the following format:

```
Title: [title]
Content: [content]
```

Implement a Discord bot command `template` that takes the title of the document as user input, calls the `create_template_file` function with the provided title, and sends the generated template file as a message in the Discord channel. The title can contain spaces.
"""

def create_template_file(title):
    return f"Title: {title}\nContent: [content]"