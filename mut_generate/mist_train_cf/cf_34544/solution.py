"""
QUESTION:
Create a function `strip_white_space` that takes in two parameters: `data` and `content_type`. The function should strip white space from the provided data based on the `content_type`. The `content_type` can be 'notebook', 'file', or 'text'. If `content_type` is 'notebook', strip white space from the source of each code cell in the notebook. If `content_type` is 'file' and the format is 'text', strip white space from the content of the file. If `content_type` is 'text', strip white space from the provided text content. The function should return the modified `data` after stripping white space.
"""

def strip_white_space(data, content_type):
    if content_type == 'notebook':
        for cell in data['content']['cells']:
            if cell['cell_type'] == 'code':
                cell['source'] = cell['source'].strip()
    elif content_type == 'file' and data['format'] == 'text':
        data['content'] = data['content'].strip()
    elif content_type == 'text':
        data = data.strip()
    return data